from django.http import HttpResponse
from django.shortcuts import render
from .test import getweather
def index(request):
    # context = {'inputOrigin': inputOrigin, 'inputDate': inputDate}
    return render(request, 'aairline/index.html')

def result(request):
    inputOrigin = request.POST['inputOrigin']
    inputDate = request.POST['inputDate']
    cancel_percentage, status = getweather(inputOrigin, inputDate)
    return render(request, 'aairline/result.html', {'cancel_percentage': cancel_percentage,'status':status})