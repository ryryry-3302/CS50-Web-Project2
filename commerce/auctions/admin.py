from django.contrib import admin
from .models import Bid, User, Listing, WatchList, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(WatchList)
admin.site.register(Comment)
admin.site.register(Bid)