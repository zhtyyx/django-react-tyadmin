from datetime import datetime
from .models import AirQualityConcentration, AirQualityIndex
import re
import requests
from datetime import datetime
from .models import AirQualityConcentration, AirQualityIndex, Station, City   # 需要根据实际情况修改 models 导入语句中的类名。

def save_data_to_db(hourly_data):
    for data in hourly_data:
        station_name = data['name']
        pm25 = float(data['pm25'])
        pm10 = float(data['pm10'])
        ozone = float(data['o3'])
        carbon_monoxide = float(data['co'])
        sulfur_dioxide = float(data['so2'])
        nitrogen_dioxide = float(data['no2'])

        aqi_url = 'https://link.sthj.sh.gov.cn/aqi/siteAqi/rtAirData.jsp?siteId=' + data['id'] + '&rand=0.5407475346102358'

        headers_aqi_url = {
            'Accept': '*/*',
            'Referer': f'https://link.sthj.sh.gov.cn/aqi/saqi/index.jsp?id={data["id"]}',
        }

    aqidata_response = requests.get(aqi_url, headers=headers_aqi_url)
    if aqidata_response.status_code == 200:
        real_time_index = int(re.findall(r'"rtValue":(\d+)', aqidata_response.text)[0])
        quality_evaluation = re.findall('"quality":"(.*?)"', aqidata_response.text)[0]
        primary_pollutant = re.findall('"primaryPollution":"(.*?)"', aqidata_response.text)[0]

        update_time = datetime.now()

        # 创建或更新站点信息
        station_obj, _created1 = Station.objects.update_or_create(name=station_name)

        # 创建空气质量浓度对象并保存到数据库中
        concentration_obj = AirQualityConcentration.objects.create(
            pm25=pm25,
            pm10=pm10,
            ozone=ozone,
            carbon_monoxide=carbon_monoxide,
            sulfur_dioxide=sulfur_dioxide,
            nitrogen_dioxide=nitrogen_dioxide,
            update_time=update_time,
            station_name=station_obj
        )
        # 创建空气质量指数对象并保存到数据库中
        air_quality_index_obj = AirQualityIndex.objects.create(
            pm25=pm25,
            pm10=pm10,
            ozone=ozone,
            carbon_monoxide=carbon_monoxide,
            sulfur_dioxide=sulfur_dioxide,
            nitrogen_dioxide=no2,
            real_time_index=real_time_index,
            quality_evaluation=quality_evaluation,
            primary_pollutant=primary_pollutant,
            update_time=datetime.now(),
            station_name_id=station_obj.id,
            city_name_id=None,  # 根据实际情况填写城市ID，如果站点所属的城市已经存在于数据库中，则可以直接关联；否则需要先创建该城市信息。
            aqi=None  # 暂时未获取到AQI数据，因此为 None。如有必要可在代码中补充获取 AQI 的逻辑。
        )

    else:
        print(f'无法获取 {station_name} 站点的实时数据: 状态码{aqidata_response.status_code}')