# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def ui(request):
    return render(request, 'templates/qnetweb.html',{})
# Create your views here.

def channels_page(request):
    return render(request, 'net.html', {})