"""hotelsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import checkdetails, register, customer
from django.contrib.auth import views as auth_views

app_name = 'records'

urlpatterns = [
    path('check-customer-details/', checkdetails, name='checkdetailsview'),
    path('customer-records/', customer, name='customerview'),
    path('register-records/', register, name='registerview'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logoutview')
]
