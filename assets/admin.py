from django.contrib import admin
from assets import models


class NewAssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'sn', 'manufacturer', 'model', 'c_time', 'm_time']
    list_filter = ['asset_type', 'manufacturer', 'model', 'c_time']
    search_fields = ('sn',)

    actions = ['approve_selected_new_assets']


class AssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'name', 'status', 'approved_by', 'c_time', 'm_time']

admin.site.register(models.Asset, AssetAdmin)
admin.site.register(models.Server)
admin.site.register(models.StorageDevice)
admin.site.register(models.SecurityDevice)
admin.site.register(models.BusinessUnit)
admin.site.register(models.Contract)
admin.site.register(models.CPU)
admin.site.register(models.Disk)
admin.site.register(models.EventLog)
admin.site.register(models.IDC)
admin.site.register(models.Manufacturer)
admin.site.register(models.NetworkDevice)
admin.site.register(models.NIC)
admin.site.register(models.RAM)
admin.site.register(models.SoftWare)
admin.site.register(models.Tag)
admin.site.register(models.NewAssetApprovalZone, NewAssetAdmin)
