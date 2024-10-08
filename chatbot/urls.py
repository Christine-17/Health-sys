from django.urls import path
from .views import chatbot_view
from . import views

urlpatterns = [
    path('', chatbot_view, name='chatbot'),
    path('about/', views.about_view, name='about'),
    path('dashboard/', views.home_view, name='dashboard'),
    path('online_shopping/', views.online_shopping_view, name='online_shopping'), 
    path('contact/', views.contact_view, name='contact'),
    path('online_counselling/', views.online_counselling, name='online_counselling'),
    path('cart/', views.cart_view, name='cart'),
     path('upload_prescription/', views.upload_prescription_view, name='upload_prescription'),
    path('schedule_counselling/', views.schedule_counselling_view, name='schedule_counselling'),
    path('contact/submit/', views.contact_form_submit, name='contact_form_submit'),
    path('contact/success/', views.contact_success, name='contact_success'),


]
