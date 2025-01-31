from django.urls import path
from .import views

urlpatterns = [
    path("", views.homeView, name="home"),
    path('about/', views.aboutView, name="about"),
    path("contact/", views.contactView, name="contact"),
    path("faculity/", views.facultyView, name="faculity"),
    path("courses/", views.coursesView, name="courses"),
    path("gallery/", views.gallery, name="gallery"),
    path("rules&regulations/", views.rules, name="rules"),
    path("facilities/", views.facilities, name="facility"),
    path("msgAuth/", views.authMsgs, name="authority_messages"),
    path('adMsg/' , views.adMsg , name = 'adMsg'),
    path('digMsg/' , views.digMsg , name = 'digMsg'),
    path('admission_procedure/', views.admission_procedure, name="admission_procedure"),
    path('announcement/', views.announcement, name="announcement"),
    path('admission/', views.admission, name="admission"),
    path("status/", views.status, name="status"),
    path('pay/' , views.payment_view , name='pay'),
    path("user.is_admission_taken == True/", views.pending, name="pending"),
    path("show_pdf/", views.show_pdf, name="show_pdf"),
]