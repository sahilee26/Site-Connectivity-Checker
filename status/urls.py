from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^status/', views.status, name='status'),
    path('insights/', views.insights, name="insights"),
]
