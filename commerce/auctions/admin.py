from django.contrib import admin
from .models import User, Listing, WatchList

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(WatchList)