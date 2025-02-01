from django.urls import path
from . import views

urlpatterns = [
    path("admission_form/", views.AdmissionFormsCreate.as_view(), name="admission-form-view"),
    path("admission_form/<int:pk>/", views.AdmissionFormRetriveUpdateDestroy.as_view(), name="update")
]
