from django.shortcuts import render,redirect
from bs4 import BeautifulSoup as BS
import requests
from .models import Links
# Create your views here.
def scrape(request):
    if request.method=='POST':
        page=requests.get(request.POST.get('url',''))
        data=BS(page.text,'html.parser')
        
        for link in data.find_all('a'):
            Links(address=link.get('href'),name=link.string).save()
        
    data=Links.objects.all()
    return render(request,'myapp/result.html',{'links':data})

def delete(request):
    links=Links.objects.all()
    for link in links:
        link.delete()
    return redirect('/')