"""RUN_BBPT URL Configuration

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
from django.urls import path
from run.views import UserInfoAPIView,UserInfoAPIView2,GroupInfoAPIView,GroupMemberAPIView,RunInfoAPIView,GroupAPIView,GroupUserAPIView,CreateGroupView,VIPRankView,UserTokenAPIView
from run import views as runviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiUser/',UserInfoAPIView.as_view(),name="user"),
    path('apiUser2/',UserInfoAPIView2.as_view(),name="user2"),
    path('login/', runviews.login),
    path('signup/', runviews.signup),
    path('apiGroup/',GroupInfoAPIView.as_view(),name="group"),
    path('createGroup/', CreateGroupView.as_view(),name="createGroup"),
    path('haveGroup/', runviews.haveGroup),
    path('joinGroup/', runviews.joinGroup),
    path('exitGroup/', runviews.exitGroup),
    path('apiGroupMember/',GroupMemberAPIView.as_view(),name="groupMember"),
    path('apiRunInfo/',RunInfoAPIView.as_view(),name="runInfo"),
    path('getGroupID/',GroupAPIView.as_view(),name="groupID"),
    path('whichGroup/',GroupUserAPIView.as_view(),name="GroupUser"),
    path('vip/',VIPRankView.as_view(),name="vip"),
    path('getToken/',UserTokenAPIView.as_view(),name="getToken"),
    path('getApplication/',runviews.GetApplication),
    path('checkApplication/',runviews.CheckApplication),
]