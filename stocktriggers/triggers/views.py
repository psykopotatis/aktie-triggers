from django.shortcuts import render
from .models import Stock
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StockTrigger
from .serializers import StockTriggerSerializer


def index(request):
    stocks = Stock.objects.prefetch_related("triggers").all().order_by("namn")
    return render(request, 'triggers/index.html', {'stocks': stocks})

@api_view(['GET'])
def trigger_list(request):
    triggers = StockTrigger.objects.select_related('stock').order_by('trigger_datum')
    serializer = StockTriggerSerializer(triggers, many=True)
    return Response(serializer.data)