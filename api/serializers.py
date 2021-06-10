from rest_framework import serializers
from api.models import *

class TesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TesterModel
        fields = (
            '__all__'
        )

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = (
            '__all__'
        )

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = (
            '__all__'
        )

class HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardwareModel
        fields = (
            '__all__'
        )