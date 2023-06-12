import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from tyadmin_api_cli.fields import richTextField

# Create your models here.

class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )

    gender = models.CharField(max_length=6, verbose_name="性别", choices=GENDER_CHOICES, default="female")
    image = models.ImageField(max_length=100, verbose_name="头像")

    class Meta:
        verbose_name = "user"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    area = models.FloatField()
    english_name = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='city_images/')
    super_admin = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        app_label = 'demo'



class Region(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    area = models.FloatField()
    zip_code = models.CharField(max_length=10)
    super_admin = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)


class Station(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    super_admin = models.ForeignKey(UserProfile, on_delete=models.CASCADE)



class AirQualityConcentration(models.Model):
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    ozone = models.FloatField()
    carbon_monoxide = models.FloatField()
    sulfur_dioxide = models.FloatField()
    nitrogen_dioxide = models.FloatField()
    update_time = models.DateTimeField()
    station_name = models.ForeignKey('Station', on_delete=models.CASCADE)


class AirQualityIndex(models.Model):
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    ozone = models.FloatField()
    carbon_monoxide = models.FloatField()
    sulfur_dioxide = models.FloatField()
    nitrogen_dioxide = models.FloatField()
    real_time_index = models.IntegerField()
    quality_evaluation = models.CharField(max_length=50)
    primary_pollutant = models.CharField(max_length=50)
    station_name = models.ForeignKey('Station', on_delete=models.CASCADE)
    city_name = models.ForeignKey('City', on_delete=models.CASCADE)
    aqi = models.IntegerField()
    update_time = models.DateTimeField()

