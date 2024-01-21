from django.urls import path
from quick_app import views

app_name = 'App_Order'


urlpatterns = [
    path('', views.home, name='home')
]
