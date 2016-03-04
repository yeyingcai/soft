#coding=utf-8
#forms.py
from django import forms

class Host_info(forms.Form):
    h_name = forms.CharField(max_length=50)
    h_ip = forms.IPAddressField()
    h_cpu = forms.CharField(max_length=10)
    h_mem = forms.CharField(max_length=10)


class command_form(forms.Form):
    cmd = forms.CharField()
    hosts = forms.CharField()
    stdout = forms.CharField(max_length=1000)

