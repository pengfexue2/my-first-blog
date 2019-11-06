#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-10-30 21:10

__author__ = 'Ted'


from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
]