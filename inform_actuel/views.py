from django.conf import settings
from django.shortcuts import  render



def home(request):
    return render(request, 'base/base.html', {'STATIC_URL': settings.STATIC_URL})


def detail(request):
    return render(request, 'html/details.html', {'STATIC_URL': settings.STATIC_URL})


