from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlisting", views.create_new_listing, name="create_new_listing"),
    path("listingcreated", views.listing_created, name="listing_created"),
    path("listing/<int:id>", views.show_listing, name="show_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing/rmv/<int:id>", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("listing/add/<int:id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("listing/bid/<int:id>", views.bid_on_listing, name="bid_on_listing"),
]
