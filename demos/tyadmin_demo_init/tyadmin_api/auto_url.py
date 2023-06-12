from tyadmin_api import auto_views
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
    
router = DefaultRouter(trailing_slash=False)
    
router.register('permission', auto_views.PermissionViewSet)
    
router.register('group', auto_views.GroupViewSet)
    
router.register('content_type', auto_views.ContentTypeViewSet)
    
router.register('user_profile', auto_views.UserProfileViewSet)
    
router.register('city', auto_views.CityViewSet)
    
router.register('water', auto_views.WaterViewSet)
    
router.register('region', auto_views.RegionViewSet)
    
router.register('station', auto_views.StationViewSet)
    
router.register('air_quality_concentration', auto_views.AirQualityConcentrationViewSet)
    
router.register('air_quality_index', auto_views.AirQualityIndexViewSet)
    
urlpatterns = [
        re_path('^', include(router.urls)),
    ]
    