from itertools import product
from pickletools import TAKEN_FROM_ARGUMENT4
from turtle import title
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


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
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00, blank=True)
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
    open = models.BooleanField(default='True')
#set to foreign key for future bids model :D
    winning_bid =  models.ForeignKey(
        'Bid',
        on_delete=models.CASCADE, 
        null=True,
        blank=True

    )
    
class WatchList(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        'Listing',
        on_delete=models.CASCADE,
    )

class Comment(models.Model):
    poster = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    on_product = models.ForeignKey(
        'Listing',
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=400)
    post_time = models.DateTimeField(auto_now_add=True, blank=True)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        
        self.post_time = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

class Bid(models.Model):

    bidder = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    on_product = models.ForeignKey(
        'Listing',
        on_delete=models.CASCADE,
    )

    bid_time = models.DateTimeField(auto_now_add=True, blank=True)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.post_time = timezone.now()
        return super(Bid, self).save(*args, **kwargs)
    
    bid = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    winner = models.BooleanField(default='False')

