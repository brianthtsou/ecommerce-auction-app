from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    listing_name = models.CharField(max_length=64)
    listing_price = models.DecimalField(max_digits=8, decimal_places=2)
    listing_desc = models.CharField(max_length=1000, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Bid(models.Model):
    bid_price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

