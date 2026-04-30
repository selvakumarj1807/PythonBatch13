from rest_framework import serializers
from .models import StaffEnquiry, StudentEnquiry

class StudentEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnquiry
        fields = '__all__'
        
class StaffEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffEnquiry
        fields = '__all__'