

'''
  @author Karan Dave  
'''

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('Aprofile/', views.Aprofile, name="Aprofile"),
    path('order/', views.order, name="order"),
   
]
