from django.contrib import admin
from import_export import resources
import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class AppSoftwareResource(resources.ModelResource):
    class Meta:
        model = models.AppSoftware
        
 
class ServerLevelResource(resources.ModelResource):
    class Meta:
        model = models.ServerLevel
        
class GroupsResource(resources.ModelResource):
    class Meta:
        model = models.Groups

class DataCenterResource(resources.ModelResource):
    class Meta:
        model = models.DataCenter
        
class ServiceLinesResource(resources.ModelResource):
    class Meta:
        model = models.ServiceLines    

class DomainNameResource(resources.ModelResource):
    class Meta:
        model = models.DomainName   
        
class BcpServersResource(resources.ModelResource):
    
    class Meta:
        model = models.BcpServers
                
class ServersResource(resources.ModelResource):
    class Meta:
        model = models.Servers
                
                
class AppSoftwareAdmin(admin.ModelAdmin):
    resource_class = AppSoftwareResource
    list_display=('name',)    
class ServerLevelAdmin(admin.ModelAdmin):
    resource_class = ServerLevelResource
    list_display = ['name',]
        
class GroupsAdmin(admin.ModelAdmin):
    resource_class = GroupsResource
    list_display = ['name']
class DataCenterAdmin(admin.ModelAdmin):
    resource_class = DataCenterResource
    list_display = ['name']
        
class ServiceLinesAdmin(admin.ModelAdmin):
    resource_class = ServiceLinesResource
    list_display = ['name']

class DomainNameAdmin(admin.ModelAdmin):
    resource_class = DomainNameResource  
    list_display = ['domain_name','internal_ipaddr','external_ipaddr','bcp_ipaddr','BCP_server','server']    

class BcpServersAdmin(admin.ModelAdmin):
    resource_class = BcpServersResource
    list_display = ['hostname','location']
    
class ServersAdmin(admin.ModelAdmin):
    resource_class = ServersResource   
    list_display = ['hostname','memory','cpu','bcpserver','serviceline','location','group','level','softwares']
                
admin.site.register(models.AppSoftware, AppSoftwareAdmin)
admin.site.register(models.ServerLevel, ServerLevelAdmin)   
admin.site.register(models.Groups, GroupsAdmin)   
admin.site.register(models.DataCenter, DataCenterAdmin)   
admin.site.register(models.ServiceLines, ServiceLinesAdmin)   
admin.site.register(models.DomainName, DomainNameAdmin)
admin.site.register(models.BcpServers, BcpServersAdmin)   
admin.site.register(models.Servers, ServersAdmin)   
