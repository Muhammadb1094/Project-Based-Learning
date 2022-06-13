from django.urls import path
from . import views

urlpatterns = [

    path('', views.home_view, name=''),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
]