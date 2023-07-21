from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User
from . import util
class NewListingForm(forms.Form):
    list_name = forms.CharField(label="Listing Name")
    list_price = forms.DecimalField(max_digits=8, decimal_places=2, label="Starting Price")
    list_desc = forms.CharField(widget=forms.Textarea, label="Listing Description")

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
        util.create_listing(list_name, list_price, list_desc)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        # this may work instead!!
        # p = Person(name=name, phone_number=number, date_subscribed=datetime.now(), messages_received=0)
        # p.save()
        return None
