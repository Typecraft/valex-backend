from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'login/', views.login_user),
    url(r'users/', include(router.urls))
]