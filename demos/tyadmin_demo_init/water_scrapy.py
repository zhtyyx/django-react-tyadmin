import requests
import xml.etree.ElementTree as ET
from datetime import datetime

import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tyadmin_demo.settings')

django.setup()

import requests
from bs4 import BeautifulSoup
# get_data_from_page()
from tyadmin_demo import settings
from demo.models import Water, City, Region, UserProfile

url = 'https://data.sh.gov.cn/interface/AB9102015008/14507'
headers = {
    'content-type': 'application/xml',
    'token': '2030c0cb065f3f0708fbd99429b53169'
}

import datetime

start_date = datetime.date(2021, 8, 30)
end_date = datetime.date(2023, 6, 12)

delta = end_date - start_date

for i in range(delta.days + 1):
    day = start_date + datetime.timedelta(days=i)
    print(day.strftime("%Y-%m-%d"))
    data = '<map><datatime>{}</datatime><limit>20</limit><offset>0</offset></map>'.format(day.strftime("%Y-%m-%d"))
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        result_str = response.text

        # 使用ElementTree解析XML格式字符串
        root = ET.fromstring(result_str)

        # 获取所有Data节点，并遍历输出每条记录信息
        for data_node in root.findall('.//Result/datas/Data'):
            ststationname_node = data_node.find('ststationname')
            datavalue_node = data_node.find('datavalue')
            datatime_node = data_node.find('datatime')
            ststationid_node = data_node.find('ststationid')

            if ststationname_node is not None and datavalue_node is not None and \
                    datatime_node is not None and ststationid_node is not None:
                print(
                    f"站点名称：{ststationname_node.text}，水量值：{datavalue_node.text}，监测时间：{datatime_node.text}，"
                    f"站点编号:{ststationid_node.text}")
            water_obj, _created1 = Water.objects.get_or_create(site_no=ststationname_node.text,
                                                               city=City.objects.get(id=2),
                                                               water_amount=datavalue_node.text,
                                                               create_time=datatime_node.text,
                                                               super_admin_id=UserProfile.objects.get(
                                                                   id=4).id)
    else:
        print('请求失败，状态码：', response.status_code)
