from django.conf.urls import url
from rest_framework.compat import include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import LemmaViewSet, MeaningViewSet, ValenceFrameViewSet, MeaningValenceViewSet, ExampleViewSet, \
    api_token_auth_session, UserViewSet

router = DefaultRouter()
router.register(r'lemmas', LemmaViewSet)
router.register(r'meanings', MeaningViewSet)
router.register(r'valence-frames', ValenceFrameViewSet)
router.register(r'meaning-valences', MeaningValenceViewSet)
router.register(r'examples', ExampleViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^api-token-auth-session/', api_token_auth_session),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url('^', include(router.urls))
]
