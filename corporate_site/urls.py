"""
URL configuration for corporate_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('consulting/', views.consulting, name='consulting'),
    path('career/', views.career, name='career'),
    path('bpo/', views.bpo, name='bpo'),
    path('bpo-detail/', views.bpodetail, name='bpodetail'),
    path('case/', views.case, name='case'),
    path('case-detail/', views.case_detail, name='case_detail'),
    path('cultivation/', views.cultivation, name='cultivation'),
    path('product-detail/', views.product_detail, name='product_detail'),
    path('company/', views.company, name='company'),
    path('recruit/', views.recruit, name='recruit'),
    # path('cultivation-detail/', views.cultivation_detail, name='cultivation_detail'),
    # path('cultivation-detail-2/', views.cultivation_detail_2, name='cultivation_detail_2'),
    path('admin/', admin.site.urls),
]
