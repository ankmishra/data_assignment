from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/users/', views.ApiList.as_view()),
    path('api/users/<int:pk>/', views.ApiDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)