from rest_framework import serializers
from .models import StudentAdmissionForms

class StudentAdmissionFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAdmissionForms
        fields = ["id", "first_name", "last_name", "phone_number", "posted_date"]
