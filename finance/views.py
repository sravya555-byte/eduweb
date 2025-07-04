from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#functionbased views
def feeCollection(request):
    return HttpResponse("<h1>i will collect the fee collection  from this View</h1>")

def feeDuesReport(request):
    return HttpResponse("<h1>i will get fee dues report from this view </h1>")

def feeCollectionReport(request):
    return HttpResponse("<h1>i will get fee collection report</h1>")
