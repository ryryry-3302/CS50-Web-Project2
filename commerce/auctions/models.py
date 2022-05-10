from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    
    HOME = 'HO'
    ELECTRONICS = 'EL'
    SPORTS = 'SO'
    TOYS = 'TO'
    FASHION = 'FA'

    types = [
        (HOME, 'Home'),
        (ELECTRONICS, 'Electronics'),
        (SPORTS, 'Sports'),
        (TOYS, 'Toys'),
        (FASHION, 'Fashion')
    ]


    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=400)
    start_bid =models.DecimalField(max_digits=10,decimal_places=2)
    imgurl = models.CharField(max_length=200,blank=True)
    catego = models.CharField(
        max_length=2,
        choices=types,
        blank=True
        )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    
    


