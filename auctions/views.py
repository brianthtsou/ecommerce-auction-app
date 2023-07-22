from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib import messages

from .models import *
from . import util

FASHION = "FAS"
TOYS = "TOY"
ELECTRONICS = "ELE"
HOME = "HOM"
SPORTING_GOODS = "SPO"
TOOLS_AND_PARTS = "TAP"
BOOKS = "BKS"
PET_SUPPLIES = "PET"
HEALTH_AND_BEAUTY = "HLT"
MISCELLANEOUS = "MSC"
    
CATEGORY_CHOICES = [
    (FASHION, "Fashion"),
    (TOYS, "Toys"),
    (ELECTRONICS, "Electronics"),
    (HOME, "Home"),
    (SPORTING_GOODS, "Sporting Goods"),
    (TOOLS_AND_PARTS, "Tools and Parts"),
    (BOOKS, "Books"),
    (PET_SUPPLIES, "Pet Supplies"),
    (HEALTH_AND_BEAUTY, "Health and Beauty"),
    (MISCELLANEOUS, "Miscellaneous"),
]


class NewListingForm(forms.Form):
    list_name = forms.CharField(label="Listing Name", max_length=64)
    list_price = forms.DecimalField(max_digits=8, decimal_places=2, label="Starting Price")
    list_image_url = forms.CharField(label="Image URL (optional)", max_length=2048, required=False)
    list_category = forms.ChoiceField(choices = CATEGORY_CHOICES)
    list_desc = forms.CharField(widget=forms.Textarea, label="Listing Description", max_length=1000)

def index(request):
    return render(request, "auctions/index.html")


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

def create_new_listing(request):
    return render(request, "auctions/new_listing.html", {
        "listing_form" : NewListingForm()
    })

def listing_created(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
    
    if form.is_valid():
        list_name = form.cleaned_data["list_name"]
        list_price = form.cleaned_data["list_price"]
        list_desc = form.cleaned_data["list_desc"]
        list_image_url = form.cleaned_data["list_image_url"]
        list_category = form.cleaned_data["list_category"]
        current_user = request.user
        # util.create_listing(list_name, list_price, list_desc)
        l = Listing(listing_name = list_name, listing_price=list_price, listing_desc=list_desc, 
                    image_url=list_image_url, category=list_category, user=current_user)
        l.save()
        messages.success(request, "Your listing has been created!")
        return HttpResponseRedirect(reverse("index"))
    else:
        return None
