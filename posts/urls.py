from .views import LanguageViewSet,ParadigmViewSet,ProgarammerViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('languages', LanguageViewSet)
router.register('paradigms', ParadigmViewSet)
router.register('programmers', ProgarammerViewSet)
urlpatterns = router.urls

