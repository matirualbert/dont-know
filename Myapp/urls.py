from django.urls import path
from Myapp import views
urlpatterns = [
   path('', views.home, name='my_index'),
   path('about/', views.about, name='my_about'),
   path('team/', views.team, name='my_team'),
   path('testimonials/', views.testimonials, name='my_testimonials'),
   path('contact/', views.contact, name='my_contact'),
   path('service/', views.service, name='my_service'),
   path('book/', views.book, name='my_book'),
   path('about/', views.about, name='my_about')


]