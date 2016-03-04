# _*_ coding: utf-8  _*_
from django.test import TestCase
from django.shortcuts import render,render_to_response,redirect

address = [
    {'name':'alan','sex':'男','age':'25','address':'河南省郑州市'},
    {'name':'阿西','sex':'男','age':'21','address':'河南省郑州市'},
    {'name':'sgicer','sex':'男','age':'23','address':'河南省郑州市'},
    {'name':'tidewind','sex':'男','age':'33','address':'河南省安阳市'},
    {'name':'cood','sex':'男','age':'28','address':'河南省石家庄'},
    {'name':'被机器盖','sex':'男','age':'25','address':'河南省郑州市'},
    {'name':'北斗','sex':'男','age':'10','address':'老乡河北的'}
]

def index(req):
    return render(req,'index.html',{'address': address})
