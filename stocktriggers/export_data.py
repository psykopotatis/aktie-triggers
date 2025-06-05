import json
from triggers.models import Stock, StockTrigger

data = []
for stock in Stock.objects.prefetch_related("triggers").all():
    triggers = stock.triggers.all()
    if not triggers.exists():  # ✅ Skip stocks with no triggers
        continue

    stock_data = {
        "namn": stock.namn,
        "kortnamn": stock.kortnamn,
        "orderbook_id": stock.orderbook_id,
        "valuta": stock.valuta,
        "landkod": stock.landkod,
        "marketplace": stock.marketplace,
        "senaste_pris": stock.senaste_pris,
        "market_cap_msek": stock.market_cap_msek,
        "triggers": []
    }
    for trig in triggers:
        stock_data["triggers"].append({
            "trigger_rubrik": trig.trigger_rubrik,
            "trigger_beskrivning": trig.trigger_beskrivning,
            "trigger_referens": trig.trigger_referens,
            "kurspaverkan": trig.kurspaverkan,
            "trigger_datum": trig.trigger_datum.isoformat(),
            "trigger_datum_forvantat": getattr(trig, "trigger_datum_forvantat", "")
        })
    data.append(stock_data)

with open("export_stocks_and_triggers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Export completed.")
