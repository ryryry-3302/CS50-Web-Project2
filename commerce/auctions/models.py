from itertools import product
from turtle import title
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
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    start_bid =models.DecimalField(max_digits=10, decimal_places=2)
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
#set to foreign key for future bids model :D
    owner =  models.CharField(max_length=400, blank=True)
    
class WatchList(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        'Listing',
        on_delete=models.CASCADE,
    )
    


