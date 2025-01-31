from django import http
from django.shortcuts import render, redirect
import requests
from .models import Admission, Contact, Gallery, Facultie, Announcement, Payment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import os
from django.conf import settings
from io import BytesIO
from django.http import HttpResponse, request
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


# Create your views here.

def homeView(request):
    firstfour = Announcement.objects.filter().order_by('-date_Added')[:4]

    context = {
        "firstfour" : firstfour,
    }
    
    return render(request, "home/home.html", context)

def aboutView(request):
    return render(request, "home/about.html")

def contactView(request):
    if request.method =="POST":
        name  = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if len(name)< 3 or len(email)< 3 or len(phone)< 10:
            messages.error(request, "Form submission failed")
        if len(message)< 50:
            messages.error(request, "message should contain  atleast 50 words ")
        else:
           contact=Contact(name=name, email=email, phone=phone, message=message, subject=subject)
           contact.save()
           messages.success(request , 'Your message has been submitted successfully')
           return redirect("contact")
    
    return render(request, "home/contact.html")

def facultyView(request):
    
    phyTeacher = Facultie.objects.filter(post="Physics")
    cheTeacher = Facultie.objects.filter(post="Chemistry")
    mathTeacher = Facultie.objects.filter(post="Math")
    bioTeacher = Facultie.objects.filter(post="Biology")
    assameseTeacher = Facultie.objects.filter(post="Assamese")
    englishTeacher = Facultie.objects.filter(post="English")
    StatisticsTeacher = Facultie.objects.filter(post="Statistics")
    ecoTeacher = Facultie.objects.filter(post="Economics")
    eduTeacher = Facultie.objects.filter(post="Education")
    logicphiloTeacher = Facultie.objects.filter(post="Philosophy")
    geoTeacher = Facultie.objects.filter(post="Geography")
    arthoTeacher = Facultie.objects.filter(post="Arthopology")
    socTeacher = Facultie.objects.filter(post="Sociology")
    poloticalScience = Facultie.objects.filter(post="poloticalScience")

    context = {"phyTeacher" : phyTeacher, 
               "cheTeacher" : cheTeacher,
               "mathTeacher": mathTeacher,
               "bioTeacher": bioTeacher,
               "assameseTeacher" :assameseTeacher,
               "engTeacher" :  englishTeacher,
               "StatisticTeacher" :StatisticsTeacher,
               "ecoTeacher" : ecoTeacher,
               "eduTeacher" :eduTeacher,
               "logicPhiloTeacher" : logicphiloTeacher,
               "geoTeacher" :geoTeacher,
               "arthoTeacher" : arthoTeacher,
               "socTeacher" : socTeacher,
               "poloticalScience" : poloticalScience
               }
    return render(request, "home/faculity.html", context)


def coursesView(request):
    return render(request, "home/courses.html")

def gallery(request):

    photo = Gallery.objects.all()

    context = {"photo": photo}

    return render(request, "home/gallery.html", context)

def rules(request):
    return render(request, "home/rules&regulations.html")

def facilities(request):
    return render(request, "home/facility.html")

def authMsgs(request):
    return render(request, "home/msgAuth.html")

def adMsg(request):
    return render(request , 'home/message_from_administrative.html')

def digMsg(request):
    return render(request , 'home/message_from_dignitaries.html')

def admission_procedure(request):
    return render(request, "home/admission_procedure.html")

def announcement(request):

    allanouncement = Announcement.objects.all()

    context = {
        "allanouncement" : allanouncement
    }

    return render(request, "home/announcement.html", context)


# admission views 
@login_required
def admission(request):

    currentUser = request.user


    registered_email = currentUser.email
    registered_phone = currentUser.phone

    # if user has submitted the admission form and payment has not been done
    if currentUser.is_admission_taken and currentUser.is_paid == False:
        return redirect("pay/")

    # if user has taken the admission and his payment has paid 
    elif currentUser.is_admission_taken and currentUser.is_paid == True:
        # if user has taken admission and admission is verified and Payment has been verified
        return redirect("/show_pdf/")
    
    # if user has not taken admission 
    else:
        if request.method == "POST":
            pastschool =  request.POST.get("pastschool")
            passedexam = request.POST.get("passedexam")
            roll= request.POST.get("roll")
            no = request.POST.get("no")
            board_qualified = request.POST.get("board_qualified")
            admitcard = request.FILES.get("admitcard")
            subjects = request.POST.get("subjects")
            studentname = request.POST.get("studentname")
            dateofbirth = request.POST.get("dateofbirth")
            nationality = request.POST.get("nationality")
            religion = request.POST.get("religion")
            caste = request.POST.get("caste")
            fathername  = request.POST.get("fathername")
            fatheroccupation = request.POST.get("fatheroccupation")
            fatherannualincome = request.POST.get("fatherannualincome")
            mothername  = request.POST.get("mothername")
            motheroccupation  = request.POST.get("motheroccupation")
            motherannualincome  = request.POST.get("motherannualincome")
            address1  = request.POST.get("address1")
            email  = registered_email
            gender = request.POST.get('gender')
            postOffice = request.POST.get("postoffice")
            phoneNumber = registered_phone
            pincode = request.POST.get("pincode")
            hostel = request.POST.get('hostel')
            stuPhoto  = request.FILES.get("stuPhoto")

            line = request.POST.get("line")


            admission=Admission(pastschool=pastschool,passedexam=passedexam, roll=roll, no=no, board_qualified=board_qualified, admitcard=admitcard,
            Select_sub=subjects, studentname=studentname, dateofbirth=dateofbirth,gender=gender, nationality=nationality, religion=religion, caste=caste, fathername=fathername,
            fatheroccupation=fatheroccupation, fatherannualincome=fatherannualincome, mothername=mothername, motheroccupation=motheroccupation, motherannualincome=motherannualincome,
            address1=address1, email=email, postOffice=postOffice, phoneNumber=phoneNumber, pincode=pincode, 
            stuPhoto=stuPhoto, stream=line , hostel = hostel );

            admission.save()
            currentUser.is_admission_taken = True
            currentUser.save()

            return redirect('status')
        

    return render(request, "home/admission.html", {"email": registered_email , "phone" : registered_phone})

# function for page not found 
def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error.html', data)

@login_required
def status(request):
    
    registered_user = request.user

    admission_status = registered_user.is_admission_taken
    print(admission_status)

    if admission_status:
        return render(request, "home/status.html")
    else:
        return redirect('/')

@login_required
def payment_view(request):   
    currentUser = request.user
    currentuser_email = currentUser.email
    phone_num = currentUser.phone

    # checking admission approvel of the logged user
    admission_Status = Admission.objects.get(email = currentuser_email)

    # taking admission taken value true / false
    admission_status = currentUser.is_admission_taken
    print(admission_Status)
    print(currentUser)

    # if current user admission status is True
    if admission_status:
        if admission_Status.status == "1":
            if request.method == "POST":
                pay_verify_ss = request.FILES.get("verifyss")

                payment = Payment(payment_ss=pay_verify_ss , email = currentuser_email , phone_number= phone_num)
                payment.save()
                
                currentUser.is_paid = True
                currentUser.save()
                return redirect('pending')
            return render(request , 'home/Payment.html')
               
        elif admission_Status.status == "0":
            messages.info(request, "Your admission status is on pending")
            return redirect('status')
        else:
            messages.error(request, "Sorry, Your admission form is rejected")
            return render(request, "home/message.html")
            
       
    else:
        return redirect('/')



def pending(request):
    current_user = request.user
    paid_status =   current_user.is_paid
    if paid_status:
        return render(request, "home/pending.html")
    else:
        return redirect("/")


@login_required
def show_pdf(request):
    current_user_email = request.user.email

    # getting the current user from paemnts table 
    Paid_user = Payment.objects.filter(email = current_user_email)

    # if user has taken the admission form 
    if request.user.is_admission_taken == True:
        try:
            Students = Admission.objects.get(email = current_user_email)
        except:
            return HttpResponse('Some Error has occoured')
        student_name = Students.studentname
        payment_verify = ''

        # getting the value of user verified or not 
        for i in Paid_user:
            # payment verified 
            if i.Payment_verification == '1':
                payment_verify = '1'

            #payment rejected
            elif i.Payment_verification == '2':
                payment_verify = '2'

        # if pament is rejected give user a message  
        if payment_verify == '2':  
            messages.error(request , mark_safe('Unfortunately, we cant verify your payment proof, if you have any query contact to college authority <a class="alert-link text-dark" href="/contact/">Click here</a> to vist our contact page or <a class="alert-link text-dark" href="/">Go home</a> '))
            return render(request, "home/message.html")

        # if payment proof is accepted send user to show pdf page 
        elif payment_verify == '1':
            return render(request , 'home/show_pdf.html' , {"user_name": student_name})

        # if payment proof is not checked or still in pending then give user a pending message 
        else:
            messages.info(request, mark_safe("your payment verification is on pending... wait till our admin verify your payment proof <a class='alert-link text-dark' href='/'>Go home</a>")) 
            return render(request, "home/message.html")

    # if user has not taken any admission give him a message that you have not applied for admission 
    else:
        messages.error(request  , mark_safe('You have not applied for admission <a class="alert-link text-dark" href="/admission/">Apply now</a> or <a class="alert-link text-capitalize text-dark" href="/">Go home</a>'))
        return render(request, "home/message.html")
        
# this function convert the html page to pdf 
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None



#Opens up page as PDF
class ViewPDF(View):
	def get(self, request,  *args, **kwargs):
            student_info = Admission.objects.get(email = request.user.email)
        
            data = {
                'studentname' : student_info.studentname,
                'dateofbirth' : student_info.dateofbirth,
                'caste' : student_info.caste,
                'gender' : student_info.gender,
                'address' : student_info.address1,
                'pincode' : student_info.pincode,
                'postOffice' : student_info.postOffice,
                'fathername' : student_info.fathername,
                'fatheroccupation' : student_info.fatheroccupation,
                'mothername' : student_info.mothername,
                'motheroccupation' : student_info.motheroccupation,
                'phoneNumber' : student_info.phoneNumber,
                'email' : student_info.email,
                'hostel' : student_info.hostel,
                'stream' : student_info.stream,
                'Select_sub' : student_info.Select_sub,
                'status' : student_info.status

            }
            pdf = render_to_pdf('home/pdf.html', data)
            return HttpResponse(pdf, content_type='application/pdf')

class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
            student_info = Admission.objects.get(email = request.user.email)
        
            data = {
                'studentname' : student_info.studentname,
                'dateofbirth' : student_info.dateofbirth,
                'caste' : student_info.caste,
                'gender' : student_info.gender,
                'address' : student_info.address1,
                'pincode' : student_info.pincode,
                'postOffice' : student_info.postOffice,
                'fathername' : student_info.fathername,
                'fatheroccupation' : student_info.fatheroccupation,
                'mothername' : student_info.mothername,
                'motheroccupation' : student_info.motheroccupation,
                'phoneNumber' : student_info.phoneNumber,
                'email' : student_info.email,
                'hostel' : student_info.hostel,
                'stream' : student_info.stream,
                'Select_sub' : student_info.Select_sub,
                'status' : student_info.status

            }

            pdf = render_to_pdf('home/pdf.html', data)

            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "applicationForm_%s.pdf" %(str(student_info.unique_id))
            content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response