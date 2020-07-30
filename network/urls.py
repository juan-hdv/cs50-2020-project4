
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newPost", views.newPost, name="newPost"),
    path("updatePost", views.updatePost, name="updatePost"),
    path("likePost", views.likePost, name="likePost"),
	path("profile", views.profile, name="profile"),
	path("following", views.following, name="following")
]
