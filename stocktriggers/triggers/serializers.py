from rest_framework import serializers
from .models import StockTrigger

class StockTriggerSerializer(serializers.ModelSerializer):
    aktie = serializers.CharField(source="stock.namn")

    class Meta:
        model = StockTrigger
        fields = [
            "id",
            "aktie",
            "trigger_rubrik",
            "trigger_beskrivning",
            "trigger_referens",
            "kurspaverkan",
            "trigger_datum"
        ]
