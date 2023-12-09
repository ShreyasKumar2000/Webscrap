from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup

from webscrap_app.models import links


def home(request):
    if request.method=="POST":
        enter_link=request.POST.get('page','')
        urls=requests.get(enter_link)
        beauty=BeautifulSoup(urls.text,'html.parser')
        for i in beauty.find_all('a'):
            li_address=i.get('href')
            li_name=i.string
            links.objects.create(address=li_address,stringname=li_name)
        return HttpResponseRedirect('/')
    else:
        data_values=links.objects.all()
    return render(request,'home.html',{'data_values':data_values})