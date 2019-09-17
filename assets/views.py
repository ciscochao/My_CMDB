from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def report(request):
    if request.method == "POST":
        asset_data = request.POST.get('asset_data')
        print(asset_data)
        return HttpResponse("成功收到数据！")
