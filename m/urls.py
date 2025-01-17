"""
URL configuration for m project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from mad.views import CompanyView, RoleView, UserView
from django.contrib.auth.models import User
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from mad.views import *

class OTPAdmin(OTPAdminSite):
    pass
admin_site=OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice,TOTPDeviceAdmin)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/companies/', CompanyView.as_view(), name='company'),
    path('api/v1/roles/', RoleView.as_view(), name='role'),
    path('api/v1/users/', UserView.as_view(), name='user'),
]
