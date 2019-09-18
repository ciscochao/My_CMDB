from django.contrib import admin
from assets import models
from assets import asset_handler


class NewAssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'sn', 'manufacturer', 'model', 'c_time', 'm_time']
    list_filter = ['asset_type', 'manufacturer', 'model', 'c_time']
    search_fields = ('sn',)

    actions = ['approve_selected_new_assets']

    def approve_selected_new_assets(self, request, queryset):
        # 获取被勾选的资产
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        success_online_number = 0
        # 可能会有多选
        for asset_id in selected:
            obj = asset_handler.ApproveAsset(request, asset_id)
            ret = obj.asset_online()
            if ret:
                success_online_number += 1
        # admin页面顶部提示信息
        self.message_user(request, "成功批准 %s 个资产成功上线！" % success_online_number)

    approve_selected_new_assets.short_description = "批准选择的新资产"


class AssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'name', 'status', 'approved_by', 'c_time', 'm_time']


admin.site.register(models.Asset, AssetAdmin)
admin.site.register(models.Manufacturer)
admin.site.register(models.Server)
admin.site.register(models.NetworkDevice)
admin.site.register(models.StorageDevice)
admin.site.register(models.SecurityDevice)
admin.site.register(models.BusinessUnit)
admin.site.register(models.Contract)
admin.site.register(models.CPU)
admin.site.register(models.Disk)
admin.site.register(models.IDC)
admin.site.register(models.NIC)
admin.site.register(models.RAM)
admin.site.register(models.SoftWare)
admin.site.register(models.Tag)
admin.site.register(models.EventLog)
admin.site.register(models.NewAssetApprovalZone, NewAssetAdmin)
