from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Stock

def index_template(request):
    stocks = Stock.objects.all()
    return render(request, 'logistics/stock.html', {'stocks': stocks})
