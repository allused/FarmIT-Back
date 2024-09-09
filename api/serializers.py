from dataclasses import field
from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Farm, FarmType

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
class FarmTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmType
        fields = ["id", "title", "description"]
    
class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ["id","owner", "farm_area", "trap_count", "farm_type_id", "farm_type", "farm_raw_data", "created_at"]
        extra_kwargs = {"owner": {"read_only": True}, "farm_type_id": {"write_only": True}}
