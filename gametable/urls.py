from django.urls import path

from .views import GameCreateView, update_dices, game_detail, game_add, game_remove, game_update, game_home, roll_dices

app_name = "gametable"

urlpatterns = [
    path("", game_detail, name="detail"),
    path("table/", game_home, name="table"),
    path("add/<int:character_id>>/", game_add, name="add"),
    path("update/<int:character_id>>/<str:type>", game_update, name="update"),
    path("remove/<int:character_id>/", game_remove, name="remove"),
    path("create/", GameCreateView.as_view(), name="create"),
    path("dices/", update_dices , name="dices"),
    path("roll/<int:character_id>/<int:dices>", roll_dices , name="roll"),
]