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
    company_name= serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = ProjectModel
        fields = (
            'id',
            'name',
            'company',
            'company_name',
        )

class HardwareSerializer(serializers.ModelSerializer):
    project_name= serializers.ReadOnlyField(source='project.name')
    tester_name= serializers.ReadOnlyField(source='tester.name')

    class Meta:
        model = HardwareModel
        fields = (
            'id',
            'name',
            'status',
            'notes',
            'project',
            'project_name',
            'tester',
            'tester_name',
        )