from django.urls import path

from .views import custom_login

app_name = "pages"

urlpatterns = [
    path("", custom_login, name="home"),
]