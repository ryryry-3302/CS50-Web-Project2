from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<int:list_id>", views.listing, name="listingpage"),
    path("edit/<int:list_id>", views.edit, name="edit"),
    path("mylist", views.mylist, name="mylist"),
    path("addcomment", views.addcomment, name="addcomment"),

]
