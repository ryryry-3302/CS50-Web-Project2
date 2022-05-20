from itertools import product
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from .models import User, Listing, WatchList


class ListingForm(forms.ModelForm):
        # specify the name of model to use
        class Meta:
            model = Listing
            exclude = ['user'], ['price']



def index(request):
    listings = Listing.objects.all()

    return render(request, "auctions/index.html",
    {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.user.is_authenticated == False:
        return HttpResponseRedirect(reverse("index"))
        

    form = ListingForm(request.POST or None, request.FILES or None)
    f = ListingForm(request.POST)
    if f.is_valid():
        # save the form data to model
        result = f.save(commit=False)
        result.user = request.user
        result.save()
        
    if request.method == 'POST':
        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html", {
        'form': form
    })

def listing(request ,list_id):
    if request.method == "POST":
        if request.user.is_authenticated == True:
            print("hi")
            listing_to_add = Listing.objects.get(pk=list_id)
            print(listing_to_add)
            l = WatchList(user=request.user, product=listing_to_add)
            print(l)
            l.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            print("pepega")
            return HttpResponseRedirect(reverse("index"))

    if Listing.objects.filter(pk=list_id).exists():
        inlist = True
        if WatchList.objects.filter(user=request.user, product=Listing.objects.get(pk=list_id)).exists():
            inlist = False
        return render(request, "auctions/listing.html", {
            "listing" : Listing.objects.get(pk=list_id),
            "inlist" : inlist,
        })
    else:
        return HttpResponseRedirect(reverse("index"))

@login_required
def edit(request, list_id):
    if Listing.objects.filter(pk=list_id).exists():
        editlisting = Listing.objects.get(pk=list_id)
        f = ListingForm(instance=editlisting)
        if f.is_valid():
        # save the form data to model
            result = f.save(commit=False)
            result.user = request.user
            result.save()
        

        if request.method == 'POST':
            f = ListingForm(request.POST, instance=editlisting)
            if f.is_valid():
            # save the form data to model
                result = f.save(commit=False)
                result.user = request.user
                result.save()
            return HttpResponseRedirect(reverse("index"))

        return render(request, "auctions/edit.html", {
            'form': f
        })
    else:
        return HttpResponseRedirect(reverse("index"))