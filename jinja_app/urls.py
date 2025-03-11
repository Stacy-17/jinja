from django.urls import path
from jinja_app import views

urlpatterns = [
  path('', views.index, name='my_index'),
  path('about/', views.about, name='my_about'),
  path('contact/', views.contact, name='my_contact'),
  path('services/', views.services, name='my_services'),
]