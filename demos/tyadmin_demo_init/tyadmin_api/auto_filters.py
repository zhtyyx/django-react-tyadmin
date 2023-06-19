from django_filters import rest_framework as filters
from tyadmin_api.custom import DateFromToRangeFilter
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from demo.models import UserProfile, City, Water, Region, Station, AirQualityConcentration, AirQualityIndex

class PermissionFilter(filters.FilterSet):
    content_type_text = filters.CharFilter(field_name="content_type")

    class Meta:
        model = Permission
        exclude = []

class GroupFilter(filters.FilterSet):

    class Meta:
        model = Group
        exclude = []

class ContentTypeFilter(filters.FilterSet):

    class Meta:
        model = ContentType
        exclude = []

class UserProfileFilter(filters.FilterSet):
    last_login = DateFromToRangeFilter(field_name="last_login")
    date_joined = DateFromToRangeFilter(field_name="date_joined")

    class Meta:
        model = UserProfile
        exclude = ["image","image"]

class CityFilter(filters.FilterSet):
    super_admin_text = filters.CharFilter(field_name="super_admin")

    class Meta:
        model = City
        exclude = ["image","image"]

class WaterFilter(filters.FilterSet):
    super_admin_text = filters.CharFilter(field_name="super_admin")
    city_text = filters.CharFilter(field_name="city")
    update_time = DateFromToRangeFilter(field_name="update_time")
    create_time = DateFromToRangeFilter(field_name="create_time")

    class Meta:
        model = Water
        exclude = []

class RegionFilter(filters.FilterSet):
    super_admin_text = filters.CharFilter(field_name="super_admin")
    city_text = filters.CharFilter(field_name="city")

    class Meta:
        model = Region
        exclude = []

class StationFilter(filters.FilterSet):
    region_text = filters.CharFilter(field_name="region")
    city_text = filters.CharFilter(field_name="city")
    super_admin_text = filters.CharFilter(field_name="super_admin")

    class Meta:
        model = Station
        exclude = []

class AirQualityConcentrationFilter(filters.FilterSet):
    station_name_text = filters.CharFilter(field_name="station_name")
    update_time = DateFromToRangeFilter(field_name="update_time")

    class Meta:
        model = AirQualityConcentration
        exclude = []

class AirQualityIndexFilter(filters.FilterSet):
    station_name_text = filters.CharFilter(field_name="station_name")
    city_name_text = filters.CharFilter(field_name="city_name")
    update_time = DateFromToRangeFilter(field_name="update_time")

    class Meta:
        model = AirQualityIndex
        exclude = []