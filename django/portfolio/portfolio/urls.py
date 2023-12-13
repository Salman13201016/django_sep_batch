"""portfolio URL Configuration

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
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index1),
    path('admin/facts',views.facts,name='facts'),
    path('admin/about',views.about_index,name='about'),
    path('admin/about/insert',views.about_insert,name='about_insert'),
    path('admin/about/facts',views.f_insert,name='facts_insert'),
    path('admin/about/delete/<int:u_id>',views.about_delete,name='delete_about'),
    path('admin/about/edit/<int:u_id>',views.about_edit,name='edit_about'),
    path('admin/about/edit/',views.about_edit_f,name='edit_about_f'),
]
