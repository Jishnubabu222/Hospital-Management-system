"""
URL configuration for hospmini project.

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
from.import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.display),
    path('login',views.login),
    path('signup',views.signup),
    path('home',views.home),
    path('signupdb',views.hospitalsignup),
    path('loginfn',views.login_func),
    path('logout',views.logout),
    path('booking',views.bookingapp),
    path('adminlog',views.adminlogin),
    path('details',views.booking_dtl),
    path('adminhome',views.adminhome),
    path('adminlogin',views.adminlog),
    path('adminlogout',views.adminlogout),
    path('appoinment',views.adminappoinment),
    path('approveapp/<id>',views.acceptapp),
    path('rejectapp/<id>',views.rejectapp),
    path('docsform',views.docsform),
    path('docs_add',views.docs_add),
    path('docDisplay',views.docDisplay),
    path('docDele/<id>',views.docDele)
]
