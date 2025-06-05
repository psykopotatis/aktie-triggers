import json
from datetime import datetime
from triggers.models import Stock, StockTrigger

with open("export_stocks_and_triggers_modified.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for stock_item in data:
    stock, _ = Stock.objects.update_or_create(
        namn=stock_item["namn"],
        defaults={
            "kortnamn": stock_item["kortnamn"],
            "orderbook_id": stock_item["orderbook_id"],
            "valuta": stock_item["valuta"],
            "landkod": stock_item["landkod"],
            "marketplace": stock_item["marketplace"],
            "senaste_pris": stock_item["senaste_pris"],
            "market_cap_msek": stock_item["market_cap_msek"],
        }
    )

    for trig_item in stock_item.get("triggers", []):
        StockTrigger.objects.update_or_create(
            stock=stock,
            trigger_rubrik=trig_item["trigger_rubrik"],
            trigger_datum=datetime.strptime(trig_item["trigger_datum"], "%Y-%m-%d").date(),
            defaults={
                "trigger_beskrivning": trig_item["trigger_beskrivning"],
                "trigger_referens": trig_item["trigger_referens"],
                "kurspaverkan": trig_item["kurspaverkan"],
                "trigger_datum_forvantat": trig_item.get("trigger_datum_forvantat", "")
            }
        )
