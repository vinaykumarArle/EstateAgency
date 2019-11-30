"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('addProperty',views.addProperty,name='addProperty'),
    path('about',views.about,name='about'),
    path('newProperty',views.newProperty,name='newProperty'),
    path('viewProperty',views.viewProperty,name='viewProperty'),
    path('agentSingle/<int:agentId>',views.agentSingle,name='agentSingle'),
    path('agent-single',views.agentsingle,name='agent-single'),
    path('adminPanel',views.adminPanel,name='adminPanel'),
    path('addAgent',views.addAgent,name='addAgent'),
    path('addNewAgent',views.addNewAgent,name='addNewAgent'),
    path('agentList',views.agentList,name='agentList'),
    path('editAgent/<int:agentId>',views.editAgent,name='editAgent'),
    path('editAgent/updateAgent/<int:agentId>',views.updateAgent,name='updateAgent'),
    path('deleteAgent/<int:agentId>',views.deleteAgent,name='deleteAgent'),
    path('userRegister',views.userRegister,name='userRegister'),
    path('addUser',views.addUser,name='addUser'),
    path('user-login',views.userLogin,name='userLogin'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('contact',views.contact,name='contact'),
    path('contac',views.contac,name='contac'),
    path('query',views.query,name='query'),
    path('deleteQuery/<int:contsId>',views.deleteQuery,name='deleteQuery'),
    path('editProperty/<int:propId>',views.editProperty,name='editProperty'),
    path('editProperty/updateProperty/<int:propId>',views.updateProperty,name='updateProperty'),
    path('deleteProperty/<int:propId>',views.deleteProperty,name='deleteProperty'),
    path('propertyGrid',views.propertyGrid,name='propertyGrid'),
    path('blog-single',views.blogSingle,name='blog-single'),
    path('agents-grid',views.agentsGrid,name='agentsGrid'),
    path('property-single',views.propertySingle,name='property-single'),

]
