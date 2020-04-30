"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# Importing views
from corona.views import home_view, about_view
from customer.views import new_customer, rem_customer, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/',home_view, name='home'),
    path('subscribe/',new_customer, name='new_customer'),
    path('about/',about, name='about'),
    path('unsubscribe/',rem_customer,name='rem_customer'),

    path('api-auth/', include('rest_framework.urls')),

    path('api/',include('corona.api.urls'))



]
