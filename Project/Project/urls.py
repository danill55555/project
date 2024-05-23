"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Help import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('user_applications/', views.user_applications, name='user_applications'),
    path('create_application/', views.create_application, name='create_application'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
