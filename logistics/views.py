from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from .models import Stock, Base,Distribution
from .forms import StockForm
from .forms import DistributionForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, 'logistics/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(username=input_username, password=input_password)
            if new_user is not None:
                login(request, new_user)
                return redirect('select_base')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'logistics/signup.html', context)

@login_required
def select_base(request):
    bases = Base.objects.all()
    context = {
        'bases' : bases,
    }
    return render(request, 'logistics/select_base.html', context)


@login_required
def home(request, base_name):
    base = get_object_or_404(Base, name_en=base_name)
    context = {
        'base': base,
    }
    return render(request, 'logistics/home.html', context)

@login_required
def stock(request, base_name):
    stocks = Stock.objects.filter(base__name_en=base_name)
    base = get_object_or_404(Base, name_en=base_name)
    context = {
        'base': base,
        'stocks': stocks,
    }
    return render(request, 'logistics/stock.html', context)

@login_required
def input_stock(request, base_name):
    base = get_object_or_404(Base, name_en=base_name)
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            stocks = Stock.objects.all()
            context = {
                'base': base,
                'stocks': stocks,
            }
        return redirect('stock', base_name=base_name)
    else:
        form = StockForm()
        context = {
            'base': base,
            'form': form,
        }
    return render(request, 'logistics/input_stock.html', context)

@login_required
def staff(request, base_name):
    base = get_object_or_404(Base, name_en=base_name)
    context = {
        'base': base,
    }
    return render(request, 'logistics/staff.html', context)

@login_required
def distribution(request, base_name):
    base = get_object_or_404(Base, name_en=base_name)
    dists = Distribution.objects.all()
    context = {
        'base': base,
        'dists': dists,
    }
    return render(request, 'logistics/distribution.html', context)


@login_required
def input_distribution(request, base_name):
    base = get_object_or_404(Base, name_en=base_name)
    if request.method == "POST":
        form = DistributionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            dists = Distribution.objects.all()
            context = {
                'base': base,
                'dists': dists,
            }
        return redirect('distribution', base_name=base_name)
    else:
        form = DistributionForm()
        context = {
            'base': base,
            'form': form,
        }
    return render(request, 'logistics/input_distribution.html', context)
