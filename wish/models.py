from django.db import models

# Create your models here.
class wishlist(models.Model):
    name=models.CharField(max_length=20)
    wish=models.CharField(max_length=100)
    date=models.DateField()
    class Meta:
        db_table='wishlist'