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

from api.views import ProfileViewSet,MaterialViewSet,MenuViewSet,StockViewSet,MenuItemViewSet,OrderMenuViewSet,MaterialItemViewSet
from rest_framework.routers import DefaultRouter

from django.contrib.auth import views as auth_views

from myapp import views as core_views
from viewflow.rest.viewset import FlowViewSet
from myapp.flows import  ManageOrderFlow
from viewflow.rest.schemas import SchemaGenerator
from viewflow.rest.viewset import FlowViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view
from viewflow.rest import views as rest

from django.conf.urls.static import static
from django.conf import settings
# flows_nsmap = {
#     'orderflow': ManageOrderFlow
# }
orderflow_urls = FlowViewSet(ManageOrderFlow).urls

# flows_nsmap = {
#     'addflow': AddStockFlow
# # }
# addflow_urls = FlowViewSet(AddStockFlow).urls

# # flows_nsmap = {
# #     'checkflow': CheckStockFlow
# # }
# checkflow_urls = FlowViewSet(CheckStockFlow).urls

router = DefaultRouter()
router.register('Profile', ProfileViewSet)
router.register('Material', MaterialViewSet)
router.register('MaterialItem', MaterialItemViewSet)
router.register('Menu', MenuViewSet)
router.register('Stock', StockViewSet)
# router.register('SumStock', SumStockViewSet)
router.register('MenuItem', MenuItemViewSet)
router.register('OrderMenu', OrderMenuViewSet)
# router.register('BuyMaterialProcess', MenuViewSet)

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
    path('menu/', core_views.menu, name='menu'),
    path('summary/', core_views.summary, name='summary'),
    path('settings/', core_views.settings, name='settings'),
    path('settings/password/', core_views.password, name='password'),
    path('go', generic.RedirectView.as_view(url='/workflow/api/', permanent=False)),
    path('workflow/api/orderflow/', include(orderflow_urls)),
    # path('workflow/api/addflow/', include((addflow_urls,'add'),namespace='addflow')),
    # path('workflow/api/addflow/', include(addflow_urls)),
    # path('workflow/api/checkflow/', include(checkflow_urls)),
    # path('', include('rest_framework.urls', namespace='rest_framework')),
    
    # path('workflow/api/',
    #     get_schema_view(generator_class=SchemaGenerator),
    #     name='index'),
    # path('workflow/api/auth/token/',
    #     obtain_auth_token,
    #     name='login'),
    # path('workflow/api/flows/',
    #     rest.FlowListView.as_view(ns_map=flows_nsmap),
    #     name="flow-list"),
    # path('workflow/api/tasks/',
    #     rest.AllTaskListView.as_view(ns_map=flows_nsmap),
    #     name="task-list"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
