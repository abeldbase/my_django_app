from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('students/<int:id>', views.students_detail),
    path('students/', views.all_students),
]
