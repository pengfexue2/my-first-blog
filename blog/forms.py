#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-11-08 10:09

__author__ = 'Ted'


from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)