from django.db import models

# Create your models here.
class Description(models.Model):
    head=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    link=models.TextField()
    rating=models.FloatField()
    price=models.IntegerField()
    offer_price=models.IntegerField()



