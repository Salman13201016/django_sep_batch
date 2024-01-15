"""reg_login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views as v

urlpatterns = [
    path('register/', v.reg,name='reg'),
    path('register/complete', v.registration_done,name="do_reg"),
    path('user/email_verification/<str:id>', v.verification,name="verification"),
    path('home/', v.home,name='home'),
    path('login/', v.login,name='login'),
    path('login/complete', v.login_done,name="do_login"),
    path('logout', v.logout,name="logout"),
]
