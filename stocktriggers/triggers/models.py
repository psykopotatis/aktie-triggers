from django.db import models

class Stock(models.Model):
    namn = models.CharField(max_length=100, unique=True)
    kortnamn = models.CharField(max_length=20)
    orderbook_id = models.CharField(max_length=20)
    valuta = models.CharField(max_length=10)
    landkod = models.CharField(max_length=2)
    marketplace = models.CharField(max_length=10)
    senaste_pris = models.FloatField()
    market_cap_msek = models.FloatField()

    def __str__(self):
        return self.namn


class StockTrigger(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="triggers")
    trigger_rubrik = models.CharField(max_length=255)
    trigger_beskrivning = models.TextField()
    trigger_referens = models.URLField()
    kurspaverkan = models.CharField(
        max_length=10,
        choices=[
            ('låg', 'Låg'),
            ('mellan', 'Mellan'),
            ('hög', 'Hög'),
            ('gigantisk', 'Gigantisk'),
        ]
    )
    trigger_datum = models.DateField()

    def __str__(self):
        return f"{self.stock.namn} – {self.trigger_rubrik}"
