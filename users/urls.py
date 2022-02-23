from django.urls import path
from . import views
from .views import *

app_name = "users"   


urlpatterns = [
    path("", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    # path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path("profile/", views.profile_request, name= "profile"),
    path("create-post/", views.create_post, name= "create_post"),
    path("all-post/", views.post_list, name= "post_list"),
    
]