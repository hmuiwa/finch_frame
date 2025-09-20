
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index, name='index'),  # Home view

    path('about/', views.about, name='about'),  # About view

    path('services/', views.services, name='services'),  # Services view

    path('contact.html', views.contact, name='contact'),  # Contact view

    path('FAQs/', views.FAQs, name='FAQs'),  # FAQs view

    path('projects/', views.projects, name='projects'),  # Projects view

    path('testimonials/', views.testimonials, name='testimonials'),  # Testimonials view

]
