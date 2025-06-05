import json
from triggers.models import Stock

with open("biotech_swe.json", "r") as f:
    data = json.load(f)

for item in data["stocks"]:
    Stock.objects.update_or_create(
        namn=item["name"],
        defaults={
            "kortnamn": item["shortName"],
            "orderbook_id": item["orderbookId"],
            "valuta": item["currency"],
            "landkod": item["countryCode"],
            "marketplace": item["marketPlaceCode"],
            "senaste_pris": item["lastPrice"],
            "market_cap_msek": item["marketCapitalization"],
        }
    )