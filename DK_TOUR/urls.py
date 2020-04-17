'''
  @author Karan Dave  
  
'''

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', include('Tbooking.urls')),
    path('home/', include('Tbooking.urls')),
    path('contact/', include('Tbooking.urls')),
    path('Account/', include('Account.urls')),
    path('msg/', include('Account.urls')),
    path('offer/', include('Account.urls')),
    path('order/', include('Account.urls')),
     path('booking_list/', include('Tbooking.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


