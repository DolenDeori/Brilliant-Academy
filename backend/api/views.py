from django.shortcuts import render
from rest_framework import generics
from .models import StudentAdmissionForms
from .serializer import StudentAdmissionFormsSerializer

# Create your views here.
class AdmissionFormsCreate(generics.ListCreateAPIView):
    queryset = StudentAdmissionForms.objects.all()
    serializer_class = StudentAdmissionFormsSerializer


class AdmissionFormRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentAdmissionForms.objects.all()
    serializer_class = StudentAdmissionFormsSerializer
    lookup_field = "pk"
