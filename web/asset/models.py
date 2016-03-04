from django.db import models

class Host(models.Model):
    h_name = models.CharField(max_length=50)
    h_ip = models.IPAddressField()
    h_cpu = models.CharField(max_length=50)
    h_mem = models.CharField(max_length=50)

    def __unicode__(self):
        return self.h_name

class command(models.Model):
    cmd = models.CharField(max_length=150)
    hosts = models.IPAddressField()
    stdout = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.cmd



