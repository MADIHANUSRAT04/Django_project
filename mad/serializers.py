from rest_framework import serializers
from .models import Company, Role, User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'features', 'created_at', 'updated_at']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'permissions', 'company', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'password', 'company', 'role', 'is_superuser', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
      
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)  
    def update(self, instance, validated_data):
        
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

