from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from assets import models
from assets import asset_handler


@csrf_exempt
def report(request):
    """
    通过csrf_exempt装饰器，跳过Django的csrf安全机制，让post的数据能被接收，但这又会带来新的安全问题。
    可以在客户端，使用自定义的认证token，进行身份验证。这部分工作，请根据实际情况，自己进行。
    :param request:
    :return:
    """
    if request.method == "POST":
        asset_data = request.POST.get('asset_data')
        data = json.loads(asset_data)
        print(asset_data)
        # 检测数据完整性
        if not data:
            return HttpResponse("无数据提交！请重试！")
        if not issubclass(dict, type(data)):
            return HttpResponse("提交的数据必须是字典格式！")
        # 通过SN号判断该资产该干嘛
        sn = data.get('sn', None)
        if sn:
            # 进入审批流程，判断是否是在线的资产
            asset_obj = models.Asset.objects.filter(sn=sn)
            if asset_obj:  # 如果是在线的SN，那么更新该资产的数据
                update_asset = asset_handler.UpdateAsset(request, asset_obj[0], data)
                return HttpResponse("已更新资产数据！")
            else:  # 如果不是在线的资产则新增资产
                obj = asset_handler.NewAsset(request, data)
                response = obj.add_to_new_assets_zone()
                return HttpResponse(response)
        else:
            return HttpResponse("没有资产SN号，请查验数据完整性！")

    return HttpResponse('200 ok')


def index(request):
    assets = models.Asset.objects.all()
    return render(request, 'assets/index.html', locals())


def dashboard(request):
    total = models.Asset.objects.count()
    upline = models.Asset.objects.filter(status=0).count()
    offline = models.Asset.objects.filter(status=1).count()
    unknown = models.Asset.objects.filter(status=2).count()
    breakdown = models.Asset.objects.filter(status=3).count()
    backup = models.Asset.objects.filter(status=4).count()
    up_rate = round(upline / total * 100)
    o_rate = round(offline / total * 100)
    un_rate = round(unknown / total * 100)
    bd_rate = round(breakdown / total * 100)
    bu_rate = round(backup / total * 100)
    server_number = models.Server.objects.count()
    networkdevice_number = models.NetworkDevice.objects.count()
    storagedevice_number = models.StorageDevice.objects.count()
    securitydevice_number = models.SecurityDevice.objects.count()
    software_number = models.SoftWare.objects.count()

    return render(request, 'assets/dashborad.html', locals())


def detail(request, asset_id):
    asset = get_object_or_404(models.Asset, id=asset_id)
    return render(request, 'assets/detail.html', locals())
