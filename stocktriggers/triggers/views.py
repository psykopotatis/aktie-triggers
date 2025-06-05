from django.shortcuts import render
from .models import Stock

def index(request):
    stocks = Stock.objects.prefetch_related("triggers").all().order_by("namn")
    return render(request, 'triggers/index.html', {'stocks': stocks})
