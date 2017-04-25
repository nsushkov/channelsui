# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def ui(request):
    return render(request, '/var/www/channelsui/net.html',{})
# Create your views here.
def hello(request):
    return HttpResponse("<b>Hello \n world1111!</b>")