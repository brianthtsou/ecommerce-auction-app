from django.contrib.auth.models import AbstractUser
from django.db import models


#TODO: add Watchlist class, fkey = user, fkey = listing

class User(AbstractUser):
    def getID(self):
        return self.id

class Listing(models.Model):
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
    
    listing_name = models.CharField(max_length=64)
    listing_price = models.DecimalField(max_digits=8, decimal_places=2)
    listing_desc = models.CharField(max_length=1000, default="")
    image_url = models.CharField(max_length=2048, default="", blank=True)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=MISCELLANEOUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.listing_name} : {self.id}"
    
    def getID(self):
        return self.id
    
    def get_info(self):
        d = {}
        d["name"] = self.listing_name
        d["price"] = self.listing_price
        d["desc"] = self.listing_desc
        d["image_url"] = self.image_url
        d["list_id"] = self.id
        return d

class Bid(models.Model):
    bid_price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


