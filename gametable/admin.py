from django.contrib import admin

from .models import Game, BattleChar

class CharsInline(admin.TabularInline):
    model = BattleChar
    extra = 6

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["pk","campaign","day","time","moon","moon_day"]
    list_editable = ["day","time","moon","moon_day"]
    inlines = [CharsInline]
 
@admin.register(BattleChar)
class BattleCharAdmin(admin.ModelAdmin):
    list_display = ["id", "game", "name", "type"]