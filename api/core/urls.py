from django.urls import path
from django.urls import include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('user/', views.UserListView.as_view(), name='user'),
]
