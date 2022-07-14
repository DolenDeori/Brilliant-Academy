from django.db import models
from django.db.models import deletion
import requests
import json
from fast2sms.sms import send_it , url

# Create your models here.

DEPARTMENT_CHOICES = (
    ("Chemistry", "Chemistry"),
    ("Physics", "Physics"),
    ("Math", "Math"),
    ("Biology", "Biology"),
    ("Assamese", "Assamese"),
    ("English", "English"),
    ("Statistics", "Statistics"),
    ("Economics", "Economics"),
    ("Education", "Education"),
    ("logicPhilosophy", " logicPhilosophy"),
    ("Geography", "Geography"),
    ("Arthopology", "Arthopology"),
    ("Sociology", "sociology"),
    ("poloticalScience" , "poloticalScience")
)


class Contact(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=60, null=False)
    subject = models.CharField(max_length=30, null=False)
    phone =  models.CharField(null=False, max_length=12)
    message = models.TextField(max_length=500)

    def __str__(self):
        return "message from " + self.name


class Facultie(models.Model):
    name = models.CharField(max_length=60,blank=False, null=False)
    qualification = models.CharField(max_length=50,blank=False , null=False)
    image = models.ImageField(upload_to="faculity_images", blank=False , null=False)
    post = models.CharField(choices=DEPARTMENT_CHOICES, blank=False, null=False, max_length=50)


    def __str__(self):
        return self.name 


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallary_image",blank=False , null=False)




class Announcement(models.Model):

    sno = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50)
    body = models.TextField(max_length=800)
    date_Added = models.DateTimeField()
    downloadable = models.FileField(upload_to="announcement_file", blank=True , null=True)

    def __str__(self):
        return self.subject


STATUS_CHOICE = (
    ('0', 'PENDING'),
    ('1', "VERIFIED"),
    ("2", "REJECTED")
)
HOSTEL_CHOICE = (
    ('YES', 'YES'),
    ('NO', "NO")
)

class Admission(models.Model):
    pastschool = models.CharField(max_length=100, blank=False)
    passedexam = models.CharField(max_length=100, blank=False)
    

    roll = models.CharField(max_length=50, blank=False)
    no = models.CharField(max_length=50)
    board_qualified = models.CharField(max_length=10, blank=False)
    admitcard = models.FileField(upload_to='admission_images')

    studentname = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    nationality = models.CharField(max_length=30)
    religion = models.CharField(max_length=100)
    caste = models.CharField(max_length=20)

    fathername = models.CharField(max_length=80)
    fatheroccupation = models.CharField(max_length=80)
    fatherannualincome = models.CharField(max_length=100)

    mothername = models.CharField(max_length=80)
    motheroccupation = models.CharField(max_length=80)
    motherannualincome = models.CharField(max_length=100)

    address1 = models.TextField(max_length=120)
    email = models.EmailField(max_length=50, unique=True)

    postOffice = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=12)
    pincode = models.PositiveIntegerField(blank=False)
    gender = models.CharField(max_length=10)
    Select_sub = models.CharField(max_length=600)
    stream = models.CharField(max_length=20)
    hostel = models.CharField(choices=HOSTEL_CHOICE , max_length=5)

    stuPhoto = models.FileField(upload_to="admission_images")
    status = models.CharField(choices=STATUS_CHOICE, max_length=12, default=STATUS_CHOICE[0][0])


    

    def __str__(self):
        return self.studentname + " 's application" 

    # from message.sms import url , send_sms

    def save(self, *args , **kwargs):
        if self.status == "1":
            message = '125666'
            value = send_it( message , number= str(self.phoneNumber))
            response = requests.request("POST",url ,data = value[0] , headers = value[1])

        if self.status == "2":
            value = send_it('123504' , number= str(self.phoneNumber))
            response = requests.request("POST",url,data = value[0] , headers = value[1])
        return super().save(*args, **kwargs)


Payment_status = (
    ("1", "verify"),
    ("2", "rejected")
)



class Payment(models.Model):
    payment_ss = models.FileField(upload_to="payment_ss")
    Payment_verification = models.CharField(choices=Payment_status, max_length=60)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.email
    
    def save(self ,  *args , **kwargs):
        message = '124773'
        value = send_it( message , number= str(self.phone_number))
        if self.Payment_verification == "1":
            response = requests.request("POST",url ,data = value[0] , headers = value[1])
        return super().save(*args, **kwargs)