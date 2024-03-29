from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from lexicon.views import LemmaViewSet, MeaningViewSet, ValenceFrameViewSet, MeaningValenceViewSet, ExampleViewSet

router = DefaultRouter()
router.register(r'lemmas', LemmaViewSet)
router.register(r'meanings', MeaningViewSet)
router.register(r'valence-frames', ValenceFrameViewSet)
router.register(r'meaning-valences', MeaningValenceViewSet)
router.register(r'examples', ExampleViewSet)

urlpatterns = [
    url('^', include(router.urls))
]
