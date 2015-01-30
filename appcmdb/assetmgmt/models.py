#coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
from django.db import models
# Create your models here. 
class AppSoftware(models.Model):
    name = models.CharField(max_length=10,unique=True)
    class Meta:
        verbose_name = "应用软件"
        verbose_name_plural = "应用软件"
        ordering = ['id']
    def __unicode__(self):
        return self.name
    
class ServerLevel(models.Model):
    name = models.CharField(max_length= 10,unique=True)
    class Meta:
        verbose_name = "服务级别"  
        verbose_name_plural = "服务级别"
        ordering = ['id']
    def __unicode__(self):
        return self.name
    
class Groups(models.Model):
    name = models.CharField(max_length= 10,unique=True)
    desc = models.CharField(max_length=255,blank=True)
    class Meta:
        verbose_name = "服务组" 
        verbose_name_plural = "服务组"    
        ordering = ['id']        
    def __unicode__(self):
        return self.name
    
class DataCenter(models.Model):
    name = models.CharField(max_length= 20, unique=True)
    class Meta:
        verbose_name = "机房"
        verbose_name_plural = "机房"
        ordering = ['id']
    def __unicode__(self):
        return self.name
    
class ServiceLines(models.Model):
    name = models.CharField(max_length= 20, unique = True)
    group = models.ManyToManyField(Groups)
    class Meta:
        verbose_name = "业务线" 
        verbose_name_plural = "业务线"    
        ordering = ['id']
    def __unicode__(self):
        return self.name
    def groups(self):
        groups=[]
        for obj in self.group.select_related():
            groups.append(obj.name)
        return groups    
class DomainName(models.Model):    
    domain_name = models.CharField(max_length=255,unique=True)
    internal_addr = models.ForeignKey('IPaddrs')
    bcp_ipaddr = models.ForeignKey('BCPIPaddrs',blank=True)
    class Meta:
        verbose_name = "域名" 
        verbose_name_plural = "域名"
        ordering = ['id']
    def __unicode__(self):
        return self.domain_name 
    def softwares(self):
        softs=[]
        for obj in self.app_software.select_related():
            softs.append(obj.name)
        return softs    

        
class BCPIPaddrs(models.Model):
    ipaddr = models.IPAddressField(unique=True)

    class Meta:
        verbose_name = "BCPIP" 
        verbose_name_plural = "BCPIP"
        ordering = ['id']
    def __unicode__(self):
        return self.ipaddr
    
  
       
class IPaddrs(models.Model):
    ipaddr = models.IPAddressField(unique=True)       
    DMZ = models.BooleanField(default=False)
    class Meta:
        verbose_name = "IP" 
        verbose_name_plural = "IP"
        ordering = ['id']
    def __unicode__(self):
        return self.ipaddr
            

    
class BcpServers(models.Model):
    hostname =  models.CharField(max_length=255,unique=True)
    location = models.ForeignKey(DataCenter)
    bcp_ipaddr = models.ManyToManyField('BCPIPaddrs')
    class Meta:
        verbose_name = "BCP服务器"
        verbose_name_plural = "BCP服务器"      
        ordering = ['id']
    def __unicode__(self):
        return self.hostname
    def ipaddrs(self):
        ipaddrs=[]
        for obj in self.bcp_ipaddr.select_related():
            ipaddrs.append(obj.ipaddr)
        return ipaddrs

        
class Servers(models.Model):
    bcpserver = models.OneToOneField(BcpServers,null=True,blank=True)
    hostname = models.CharField(max_length=255,unique=True)
    vitual_machine = models.BooleanField(default=True)
    memory = models.CharField(max_length=20)
    cpu = models.SmallIntegerField()
    serviceline = models.ForeignKey(ServiceLines)
    location = models.ForeignKey(DataCenter)
    group = models.ForeignKey(Groups)
    level = models.ForeignKey(ServerLevel)
    app_software = models.ManyToManyField('AppSoftware')
    ip_addrs = models.ManyToManyField('IPaddrs')
    class Meta:
        ordering = ['id']
        verbose_name = "服务器"
        verbose_name_plural = "服务器"   
    def __unicode__(self):
        return self.hostname
    
    def softwares(self):
        softs=[]
        for obj in self.app_software.select_related():
            softs.append(obj.name)
        return softs
    
    def ipaddrs(self):
        ipaddrs=[]
        for obj in self.ip_addrs.select_related():
            ipaddrs.append(obj.ipaddr)
        return ipaddrs
    