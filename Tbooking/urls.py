

'''
  @author Karan Dave  
'''

from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('msg/', views.msg, name='msg'),
    path('offer/', views.offer, name='offer'),
    path('book/<int:places_pk>', views.book, name="book"),
    path('booking_list/', views.booking_list, name='booking_list'),
]
