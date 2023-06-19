from datetime import datetime

import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tyadmin_demo.settings')

django.setup()

import requests
from bs4 import BeautifulSoup
# get_data_from_page()
from tyadmin_demo import settings
from demo.models import Station, AirQualityConcentration, AirQualityIndex, City, Region, UserProfile


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
                    print(name)
                    try:
                        station_obj, _created1 = Station.objects.get_or_create(name=name, city=City.objects.get(id=2),
                                                                               region=Region.objects.get(
                                                                                   name__startswith=name[:2]),
                                                                               super_admin_id=UserProfile.objects.get(
                                                                                   id=4).id)
                    except Region.DoesNotExist:
                        continue
                    pm25 = 0 if cols[1].get_text().strip() == '-' else cols[1].get_text().strip()
                    pm10 = 0 if cols[2].get_text().strip() == '-' else cols[2].get_text().strip()
                    o3 = 0 if cols[3].get_text().strip() == '-' else cols[3].get_text().strip()
                    co = 0 if cols[4].get_text().strip() == '-' else cols[4].get_text().strip()
                    so2 = 0 if cols[5].get_text().strip() == '-' else cols[5].get_text().strip()
                    no2 = 0 if cols[6].get_text().strip() == '-' else cols[6].get_text().strip()
                    try:

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
                    except Exception as e:
                        print(e)

                for row in rows1:
                    cols = row.find_all('td')
                    name = cols[0].get_text().strip()
                    try:
                        station_obj, _created1 = Station.objects.get_or_create(name=name, city=City.objects.get(id=2),
                                                                               region=Region.objects.get(
                                                                                   name__startswith=name[:2]),
                                                                               super_admin_id=UserProfile.objects.get(
                                                                                   id=4).id)
                    except Region.DoesNotExist:
                        continue
                    pm25 = 0 if cols[1].get_text().strip() == '-' else cols[1].get_text().strip()
                    pm10 = 0 if cols[2].get_text().strip() == '-' else cols[2].get_text().strip()
                    o3 = 0 if cols[3].get_text().strip() == '-' else cols[3].get_text().strip()
                    co = 0 if cols[4].get_text().strip() == '-' else cols[4].get_text().strip()
                    so2 = 0 if cols[5].get_text().strip() == '-' else cols[5].get_text().strip()
                    no2 = 0 if cols[6].get_text().strip() == '-' else cols[6].get_text().strip()
                    real_time_index = 0 if cols[7].get_text().strip() == '-' else cols[7].get_text().strip()
                    quality_evaluation = 0 if cols[8].get_text().strip() == '-' else cols[8].get_text().strip()
                    primary_pollutants = 0 if cols[9].get_text().strip() == '-' else cols[9].get_text().strip()
                    try:
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
                            city_name_id=City.objects.get(id=2).id,
                            aqi=None
                        )
                    except Exception as e:
                        print(e)
                    print(
                        f'name: %s, pm25: %s, pm10: %s, o3: %s, co: %s, so2: %s, no2: %s, 实时指数: %s, 质量评价: %s, 首要污染物: %s' % (
                            name, pm25, pm10, o3, co, so2, no2, real_time_index, quality_evaluation,
                            primary_pollutants))
        else:

            print(f'An error occurred: {response.status_code}')


def get_district_data():
    import requests
    from bs4 import BeautifulSoup

    url = 'https://link.sthj.sh.gov.cn/aqi/subarea/subarea.jsp'

    # 发送 GET 请求，并添加必要的请求头部信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',
        'Referer': 'https://link.sthj.sh.gov.cn/aqi/indexMix.jsp'
    }
    response = requests.get(url, headers=headers)

    # 解析 HTML 页面，并查找所有 class 属性为 "subarea" 的 div 元素
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'detail-table'})
    headers = [header.text.strip() for header in table.find_all('th')]

    data_rows = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) == 4:
            data_rows.append([cell.text.strip() for cell in cells])

    print(headers)
    print(data_rows)
    print(
        [Region.objects.create(name=i[0], city=City.objects.get(id=2), super_admin=UserProfile.objects.get(id=4)) for i
         in data_rows])


get_hourly_data()
# get_district_data()
