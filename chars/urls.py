from django.urls import path

from .views import CharDetailView, CharListView

app_name = "chars"

urlpatterns = [
    path("", CharListView.as_view(), name="list"),
    path("<slug:slug>/", CharDetailView.as_view(), name="detail"),
    path("group/<slug:slug>/", CharListView.as_view(), name="list_by_group"),
]