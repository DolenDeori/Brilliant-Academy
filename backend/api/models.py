from django.db import models

# Create your models here.

class StudentAdmissionForms(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=12)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
