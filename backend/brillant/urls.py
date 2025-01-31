from os import name
from home.views import DownloadPDF, ViewPDF
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path('accounts/', include('accounts.urls')),
    path('viewPDF/' , ViewPDF.as_view() , name='viewPDF'),
    path('downloadPDF/' , DownloadPDF.as_view() , name='downloadPDF'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
handler404 = 'home.views.error_404_view'