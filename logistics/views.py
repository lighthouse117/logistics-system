from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect
from .models import Stock
from .forms import StockForm


def select_base(request):
    return render(request, 'logistics/select_base.html')


def home(request, base_name):
    context = {
        'base_name': base_name,
    }
    return render(request, 'logistics/home.html', context)


def stock(request, base_name):
    stocks = Stock.objects.all()
    context = {
        'base_name': base_name,
        'stocks': stocks,
    }
    return render(request, 'logistics/stock.html', context)


def input_stock(request, base_name):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            stocks = Stock.objects.all()
            context = {
                'base_name': base_name,
                'stocks': stocks,
            }
        return redirect('stock', kwargs=context)
    else:
        form = StockForm()
        context = {
            'base_name': base_name,
            'form': form,
        }
    return render(request, 'logistics/input_stock.html', context)


def staff(request, base_name):
    context = {
        'base_name': base_name,
    }
    return render(request, 'logistics/staff.html', context)


def distribution(request, base_name):
    context = {
        'base_name': base_name,
    }
    return render(request, 'logistics/distribution.html', context)
