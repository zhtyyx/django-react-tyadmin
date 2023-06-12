from rest_framework import serializers
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from demo.models import UserProfile, City, Water, Region, Station, AirQualityConcentration, AirQualityIndex


class ContentTypeListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ContentType
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ContentTypeCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ContentType
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class PermissionListSerializer(serializers.ModelSerializer):
    

    class ContentTypeSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = ContentType
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    content_type = ContentTypeSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Permission
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class PermissionCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Permission
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class GroupListSerializer(serializers.ModelSerializer):
    

    class PermissionSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Permission
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    permissions = PermissionSerializer(many=True)
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class GroupCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class UserProfileListSerializer(serializers.ModelSerializer):
    

    class GroupSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Group
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    groups = GroupSerializer(many=True)
    class PermissionSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Permission
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    user_permissions = PermissionSerializer(many=True)
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class UserProfileCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_password(self.validated_data['password'])
        instance.save()
        return instance        
        

class CityListSerializer(serializers.ModelSerializer):
    

    class UserProfileSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = UserProfile
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    super_admin = UserProfileSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class CityCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class WaterListSerializer(serializers.ModelSerializer):
    

    class UserProfileSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = UserProfile
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    super_admin = UserProfileSerializer()
    class CitySerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = City
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    city = CitySerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Water
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class WaterCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Water
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class RegionListSerializer(serializers.ModelSerializer):
    

    class UserProfileSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = UserProfile
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    super_admin = UserProfileSerializer()
    class CitySerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = City
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    city = CitySerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class RegionCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class StationListSerializer(serializers.ModelSerializer):
    

    class RegionSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Region
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    region = RegionSerializer()
    class CitySerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = City
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    city = CitySerializer()
    class UserProfileSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = UserProfile
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    super_admin = UserProfileSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Station
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class StationCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Station
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class AirQualityConcentrationListSerializer(serializers.ModelSerializer):
    

    class StationSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Station
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    station_name = StationSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = AirQualityConcentration
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class AirQualityConcentrationCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = AirQualityConcentration
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class AirQualityIndexListSerializer(serializers.ModelSerializer):
    

    class StationSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Station
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    station_name = StationSerializer()
    class CitySerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = City
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    city_name = CitySerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = AirQualityIndex
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class AirQualityIndexCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = AirQualityIndex
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)
