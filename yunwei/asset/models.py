from django.db import models

class ip_info(models.Model):
    h_ip = models.IPAddressField()

class Host_info(models.Model):
    h_ip = models.ForeignKey(ip_info)
    h_name = models.CharField(max_length=50,null=True,blank=True)
    h_user = models.CharField(max_length=20,default='root',null=True,blank=True)
    h_pass = models.CharField(max_length=30)
    h_mx = models.TextField(null=True,blank=True)
    h_cpu = models.CharField(max_length=20,blank=True)
    h_mem = models.CharField(max_length=20,blank=True)
    h_disk = models.CharField(max_length=30,blank=True)

    def __unicode__(self):
        return self.h_mx
class app_info(models.Model):
    h_ip = models.ForeignKey(ip_info)
    app = models.CharField(max_length=200,blank=True)

    def __unicode__(self):
        return self.h_ip

class cmd_info(models.Model):
    h_ip = models.ForeignKey(ip_info)
    com = models.CharField(max_length=200)

    def __unicode__(self):
        return self.h_ip








