"""buy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.views import generic
from material.frontend import urls as frontend_urls


from api.views import ProfileViewSet,MaterialViewSet,MenuViewSet
from rest_framework.routers import DefaultRouter

from django.contrib.auth import views as auth_views

from myapp import views as core_views

router = DefaultRouter()
router.register('Profile', ProfileViewSet)
router.register('Material', MaterialViewSet)
router.register('Menu', MenuViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',generic.RedirectView.as_view(url='/workflow/',permanent=False)),
    path('',include(frontend_urls)),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/', auth_views.LoginView.as_view(),{'template_name': 'myapp/templates/registration/login.html'}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'template_name': 'myapp/templates/registration/logout.html'}, name='logout'),
    path('home/', core_views.home, name='home'),
    path('settings/', core_views.settings, name='settings'),
    path('settings/password/', core_views.password, name='password'),
]
