from django.shortcuts import render
from django.http import HttpResponse

def test(req):
    return HttpResponse('123')
# Create your views here.
