import json
from datetime import datetime
from triggers.models import Stock, StockTrigger

"""
 # Import triggers like this
 python manage.py shell < import_triggers.py
 
"""
with open("biotech_triggers.json", "r") as f:
    triggers = json.load(f)

created = 0
skipped = 0

for item in triggers:
    stock = Stock.objects.filter(namn__iexact=item["aktie"]).first()
    if not stock:
        print(f"Stock saknas: {item['aktie']}")
        continue

    trigger_datum = datetime.strptime(item["trigger_datum"], "%Y-%m-%d").date()
    exists = StockTrigger.objects.filter(
        stock=stock,
        trigger_rubrik=item["trigger_rubrik"],
        trigger_datum=trigger_datum
    ).exists()

    if exists:
        skipped += 1
        continue

    StockTrigger.objects.create(
        stock=stock,
        trigger_rubrik=item["trigger_rubrik"],
        trigger_beskrivning=item["trigger_beskrivning"],
        trigger_referens=item["trigger_referens"],
        kurspaverkan=item["kurspaverkan"],
        trigger_datum=trigger_datum,
        trigger_datum_text=item.get("trigger_datum_text", "")  # <--- this line

    )
    created += 1

print(f"Importerade {created} nya triggers. Skippade {skipped} (dubbletter).")
