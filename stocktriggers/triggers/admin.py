from django.contrib import admin
from .models import Stock, StockTrigger

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('namn', 'kortnamn', 'senaste_pris', 'market_cap_msek')

@admin.register(StockTrigger)
class StockTriggerAdmin(admin.ModelAdmin):
    list_display = ('stock', 'trigger_rubrik', 'kurspaverkan', 'trigger_datum')
    list_filter = ('kurspaverkan',)
