from django.urls import path, include
from rest_framework.routers import DefaultRouter
from APIApp import views

router = DefaultRouter()
router.register(r'APIApp', views.APIAppViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]