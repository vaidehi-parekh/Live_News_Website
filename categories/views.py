from django.shortcuts import render
import requests
# Create your views here.
records = {}
def index(request):
    url = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=8e8b5075051e4452a9242a083f664060")
    mydata = url.json()
    records['indexdata'] = mydata
    return render(request,'index.html',records)

def all(request):
    url1 = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=8e8b5075051e4452a9242a083f664060")
    mydata1 = url1.json()
    records['alldata'] = mydata1
    return render(request,'all.html',records)

def technology(request):
    url2 = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=8e8b5075051e4452a9242a083f664060")
    mydata2 = url2.json()
    records['technologydata'] = mydata2
    return render(request,'technology.html',records)

def business(request):
    url3 = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=8e8b5075051e4452a9242a083f664060")
    mydata3 = url3.json()
    records['businessdata'] = mydata3
    return render(request,'business.html',records)

def science(request):
    url4 = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=8e8b5075051e4452a9242a083f664060")
    mydata4 = url4.json()
    records['sciencedata'] = mydata4
    return render(request,'science.html',records)

def entertainment(request):
    url5 = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=8e8b5075051e4452a9242a083f664060")
    mydata5 = url5.json()
    records['entertainmentdata'] = mydata5
    return render(request,'entertainment.html',records)

def sports(request):
    url6 = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=8e8b5075051e4452a9242a083f664060")
    mydata6 = url6.json()
    records['sportsdata'] = mydata6
    return render(request,'sports.html',records)
