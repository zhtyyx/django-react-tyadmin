from datetime import datetime
import os

import django
import requests
from bs4 import BeautifulSoup
# get_data_from_page()
from tyadmin_demo import settings
from demo.models import Station, AirQualityConcentration, AirQualityIndex

os.environ['DJANGO_SETTINGS_MODULE'] = 'tyadmin_demo.settings'

# settings.configure(DEBUG=True)

django.setup()



def get_data_from_main_page():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
    }
    url = 'https://link.sthj.sh.gov.cn/aqi/siteAqi/siteAqi.jsp'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find('table', {'id': 'siteConcenList'})

        if table is not None:
            rows = table.tbody.find_all('tr')

            for row in rows:
                cols = row.find_all('td')
                name = cols[0].get_text().strip()
                pm25 = cols[1].get_text().strip()  # 获取第2列数据（时间）
                pm10 = cols[2].get_text().strip()  # 获取第3列数据（AQI）
                o3 = cols[3].get_text().strip()  #
                co = cols[4].get_text().strip()  #
                so2 = cols[5].get_text().strip()  #
                no2 = cols[6].get_text().strip()  #

                print(f'name: %s, pm25: %s, pm10: %s, o3: %s, co: %s, so2: %s, no2: %s' % (
                    name, pm25, pm10, o3, co, so2, no2))

    else:

        print(f'An error occurred: {response.status_code}')


def get_hourly_data():
    for i in ["201", "202", "203", "204", "205", "206", "208", "209", "210", "211", "212", "213", "214", "215", "216",
              "217"]:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
        }
        url = 'https://link.sthj.sh.gov.cn/aqi/siteAqi/siteSubareaAqi.jsp?groupId=' + i

        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, "html.parser")

            table = soup.find('table', {'id': 'siteConcenList'})
            table1 = soup.find('table', {'id': 'siteAqiList'})

            if table is not None:
                rows = table.tbody.find_all('tr')
                rows1 = table1.tbody.find_all('tr')

                for row in rows:
                    cols = row.find_all('td')
                    name = cols[0].get_text().strip()

                    station_obj, _created1 = Station.objects.get_or_create(name=name)

                    pm25 = cols[1].get_text().strip()  # 获取第2列数据（时间）
                    pm10 = cols[2].get_text().strip()  # 获取第3列数据（AQI）
                    o3 = cols[3].get_text().strip()  #
                    co = cols[4].get_text().strip()  #
                    so2 = cols[5].get_text().strip()  #
                    no2 = cols[6].get_text().strip()  #
                    concentration_obj = AirQualityConcentration.objects.create(
                        pm25=pm25,
                        pm10=pm10,
                        ozone=o3,
                        carbon_monoxide=co,
                        sulfur_dioxide=so2,
                        nitrogen_dioxide=no2,
                        station_name=station_obj,
                        update_time=datetime.now(),
                    )
                    print(f'name: %s, pm25: %s, pm10: %s, o3: %s, co: %s, so2: %s, no2: %s' % (
                        name, pm25, pm10, o3, co, so2, no2))

                for row in rows1:
                    cols = row.find_all('td')
                    name = cols[0].get_text().strip()
                    station_obj, _created1 = Station.objects.get_or_create(name=name)
                    pm25 = cols[1].get_text().strip()  # 获取第2列数据（时间）
                    pm10 = cols[2].get_text().strip()  # 获取第3列数据（AQI）
                    o3 = cols[3].get_text().strip()  #
                    co = cols[4].get_text().strip()  #
                    so2 = cols[5].get_text().strip()  #
                    no2 = cols[6].get_text().strip()  #
                    real_time_index = cols[7].get_text().strip()
                    quality_evaluation = cols[8].get_text().strip()
                    primary_pollutants = cols[9].get_text().strip()

                    air_quality_index_obj = AirQualityIndex.objects.create(
                        pm25=pm25,
                        pm10=pm10,
                        ozone=o3,
                        carbon_monoxide=co,
                        sulfur_dioxide=so2,
                        nitrogen_dioxide=no2,
                        real_time_index=real_time_index,
                        quality_evaluation=quality_evaluation,
                        primary_pollutant=primary_pollutants,
                        update_time=datetime.now(),
                        station_name_id=station_obj.id,
                        city_name_id=None,  # 根据实际情况填写城市ID，如果站点所属的城市已经存在于数据库中，则可以直接关联；否则需要先创建该城市信息。
                        aqi=None  # 暂时未获取到AQI数据，因此为 None。如有必要可在代码中补充获取 AQI 的逻辑。
                    )
                    print(
                        f'name: %s, pm25: %s, pm10: %s, o3: %s, co: %s, so2: %s, no2: %s, 实时指数: %s, 质量评价: %s, 首要污染物: %s' % (
                            name, pm25, pm10, o3, co, so2, no2, real_time_index, quality_evaluation,
                            primary_pollutants))
        else:

            print(f'An error occurred: {response.status_code}')


get_hourly_data()