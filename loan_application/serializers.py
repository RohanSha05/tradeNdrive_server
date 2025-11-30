from rest_framework import serializers
from .models import LoanApplication, EmploymentInfo
from car_listing.models import CarListing

class EmploymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentInfo
        fields = '__all__'

class LoanApplicationSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=CarListing.objects.all())
    car_name = serializers.CharField(source='car.title', read_only=True)
    employment_info = EmploymentInfoSerializer() 

    class Meta:
        model = LoanApplication
        fields = '__all__'

    def create(self, validated_data):
        employment_data = validated_data.pop('employment_info') 
        loan_application = LoanApplication.objects.create(**validated_data) 
        EmploymentInfo.objects.create(loan_application=loan_application, **employment_data) 
        
        return loan_application
