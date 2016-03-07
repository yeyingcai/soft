from django.shortcuts import render,redirect
from asset.form import *
from asset.models import *

def add_host(req):
    if req.method == "POST":
        h_name = req.POST.get('h_name')
        h_ip = req.POST.get('h_ip')
        h_mem = req.POST.get('h_mem')
        h_cpu = req.POST.get('h_cpu')
        h_disk = req.POST.get('h_disk')
        h_mx = req.POST.get('h_mx')
        h_pass = req.POST.get('h_pass')
        h_user = req.POST.get('h_user')


        ip_info.objects.create(h_ip=h_ip)
        h_info = Host_info(h_name=h_name,h_mem=h_mem,h_cpu=h_cpu,h_disk=h_disk,h_mx=h_mx,h_user=h_user,h_pass=h_pass)
        h_info.h_ip=ip_info.objects.get(h_ip=h_ip)
        h_info.save()
        return redirect('/index/')
    else:
        ip = ip_form()
        hosts = Host_form()
    return render(req,'add_host.html', {'ip':ip,'hosts':hosts})


def index(req):
    ip = ip_info.objects.all()
    hosts = Host_info.objects.all()
    return render(req,'index.html',{'ip':ip,'hosts':hosts})

def disp(req,id):
    h_info = Host_info.objects.get(id=id)
    return render(req,'disp_info.html', {'h_info':h_info})
