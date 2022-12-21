from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from lab import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('study/', include('study.urls')),
    path('data/', include('data.urls')),
    path('htmx/', views.htmx_home, name='htmx'),
]
