from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('second-page/', views.second_page, name='second_page'), # เพิ่มบรรทัดนี้
]