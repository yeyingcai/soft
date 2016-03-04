# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from asset.models import *
from asset.form import Host_info
from asset.form import command_form
import paramiko
import os
import sys

default_encoding = 'utf-8'
def add_host(req):
    if req.method == 'POST':
        h_name = req.POST.get('h_name')
        h_ip = req.POST.get('h_ip')
        h_cpu = req.POST.get('h_cpu')
        h_mem = req.POST.get('h_mem')

        Host.objects.create(h_name=h_name,h_ip=h_ip,h_cpu=h_cpu,h_mem=h_mem)
        return redirect('/index/')
    else:
        form = Host_info()
        return render(req,"add_host.html",{'form':form})

def index(req):
    hosts = Host.objects.all()
    return render(req,'index.html',{'hosts':hosts})

def disp_host(req,id):
    host = Host.objects.get(id=id)
    cmd_form = command_form()
    return render(req, 'disp_host.html',{'cmd':cmd_form,'host':host})


def cmd_out(req,id):
    if req.method == 'POST':
        h_cmd = req.POST.get('cmd')
        h = Host.objects.get(id=id)
        ip = h.h_ip
        user = 'root'
        password = '123456'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip,username=user,password=password)
        stdin,stdout,stderr = ssh.exec_command('%s' % h_cmd)
        cmd_o = stdout.read()
        cmd_e = str(stderr.read())
        ssh.close()
        command.objects.create(hosts=ip,cmd=h_cmd,stdout=h_cmd)
    return render(req,'cmd_info.html',{'h_cmd':h_cmd,'ip':ip , 'cmd_o':cmd_o})

