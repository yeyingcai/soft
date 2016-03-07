#coding=utf-8
#form.py
from django import forms

class ip_info(forms.Form):
    h_ip = forms.IPAddressField()

class Host_info(forms.Form):
    h_name = forms.CharField()
    h_user = forms.CharField()
    h_pass = forms.CharField()
    h_mx = forms.CharField()
    h_cpu = forms.CharField()
    h_mem = forms.CharField()
    h_disk = forms.CharField()

class app_info(forms.Form):
    app = forms.CharField(max_length=200)

class cmd_info(forms.Form):
    com = forms.CharField(max_length=200)
