
from rest_framework import viewsets
from tyadmin_api.custom import XadminViewSet
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from demo.models import UserProfile, City, Region, Station, AirQualityConcentration, AirQualityIndex

from tyadmin_api.auto_serializers import PermissionListSerializer, GroupListSerializer, ContentTypeListSerializer, UserProfileListSerializer, CityListSerializer, RegionListSerializer, StationListSerializer, AirQualityConcentrationListSerializer, AirQualityIndexListSerializer
from tyadmin_api.auto_serializers import PermissionCreateUpdateSerializer, GroupCreateUpdateSerializer, ContentTypeCreateUpdateSerializer, UserProfileCreateUpdateSerializer, CityCreateUpdateSerializer, RegionCreateUpdateSerializer, StationCreateUpdateSerializer, AirQualityConcentrationCreateUpdateSerializer, AirQualityIndexCreateUpdateSerializer
from tyadmin_api.auto_filters import PermissionFilter, GroupFilter, ContentTypeFilter, UserProfileFilter, CityFilter, RegionFilter, StationFilter, AirQualityConcentrationFilter, AirQualityIndexFilter

    
class PermissionViewSet(XadminViewSet):
    serializer_class = PermissionListSerializer
    queryset = Permission.objects.all().order_by('-pk')
    filterset_class = PermissionFilter
    search_fields = ["name","codename"]

    def get_serializer_class(self):
        if self.action == "list":
            return PermissionListSerializer
        else:
            return PermissionCreateUpdateSerializer

    
class GroupViewSet(XadminViewSet):
    serializer_class = GroupListSerializer
    queryset = Group.objects.all().order_by('-pk')
    filterset_class = GroupFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return GroupListSerializer
        else:
            return GroupCreateUpdateSerializer

    
class ContentTypeViewSet(XadminViewSet):
    serializer_class = ContentTypeListSerializer
    queryset = ContentType.objects.all().order_by('-pk')
    filterset_class = ContentTypeFilter
    search_fields = ["app_label","model"]

    def get_serializer_class(self):
        if self.action == "list":
            return ContentTypeListSerializer
        else:
            return ContentTypeCreateUpdateSerializer

    
class UserProfileViewSet(XadminViewSet):
    serializer_class = UserProfileListSerializer
    queryset = UserProfile.objects.all().order_by('-pk')
    filterset_class = UserProfileFilter
    search_fields = ["password","username","first_name","last_name","email","gender"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserProfileListSerializer
        else:
            return UserProfileCreateUpdateSerializer

    
class CityViewSet(XadminViewSet):
    serializer_class = CityListSerializer
    queryset = City.objects.all().order_by('-pk')
    filterset_class = CityFilter
    search_fields = ["name","english_name","zip_code"]

    def get_serializer_class(self):
        if self.action == "list":
            return CityListSerializer
        else:
            return CityCreateUpdateSerializer

    
class RegionViewSet(XadminViewSet):
    serializer_class = RegionListSerializer
    queryset = Region.objects.all().order_by('-pk')
    filterset_class = RegionFilter
    search_fields = ["name","zip_code"]

    def get_serializer_class(self):
        if self.action == "list":
            return RegionListSerializer
        else:
            return RegionCreateUpdateSerializer

    
class StationViewSet(XadminViewSet):
    serializer_class = StationListSerializer
    queryset = Station.objects.all().order_by('-pk')
    filterset_class = StationFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return StationListSerializer
        else:
            return StationCreateUpdateSerializer

    
class AirQualityConcentrationViewSet(XadminViewSet):
    serializer_class = AirQualityConcentrationListSerializer
    queryset = AirQualityConcentration.objects.all().order_by('-pk')
    filterset_class = AirQualityConcentrationFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return AirQualityConcentrationListSerializer
        else:
            return AirQualityConcentrationCreateUpdateSerializer

    
class AirQualityIndexViewSet(XadminViewSet):
    serializer_class = AirQualityIndexListSerializer
    queryset = AirQualityIndex.objects.all().order_by('-pk')
    filterset_class = AirQualityIndexFilter
    search_fields = ["quality_evaluation","primary_pollutant"]

    def get_serializer_class(self):
        if self.action == "list":
            return AirQualityIndexListSerializer
        else:
            return AirQualityIndexCreateUpdateSerializer
