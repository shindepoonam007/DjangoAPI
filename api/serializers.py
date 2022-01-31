from rest_framework import serializers
from .models import SecurityQuestion,PasswordHistory ,Device 

class SecurityQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityQuestion
        fields = '__all__' 

class PasswordHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordHistory
        fields = '__all__' 

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__' 

