# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.timezone import now


def home(request):
    return render(request, "nikah/index.html", {'now': now()})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
