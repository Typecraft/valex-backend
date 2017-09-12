from django.conf.urls import url, include
from rest_framework import routers

from . import views

urlpatterns = [
    url(r'login/', views.login_user),
    url(r'logout/', views.logout_user)
]