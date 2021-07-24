from django.contrib import admin
from django.utils.timezone import now
from django.db import models
from autoslug import AutoSlugField

from chars.models import Character

class Game(models.Model):
    campaign = models.CharField("Nome da Campanha", max_length=255)
    day = models.DateField("Dia")
    time = models.TimeField("Hora")
    slug = AutoSlugField(unique=True, always_update=False, populate_from="campaign")
    notes = models.TextField("Notas Gerais", blank=True)
    dm_only = models.TextField("Notas do Mestre", blank=True)
    rolls = models.TextField("Rolagens", blank=True)
    MOON = (
        ("1","Lua Nova"), 
        ("2","Lua Crescente Crescente"), 
        ("3","Meia Lua Crescente"),
        ("4","Lua Gibosa Crescente"),
        ("5","Lua Cheia"),
        ("6","Lua Gibosa Minguante"), 
        ("7","Meia Lua Minguante"),
        ("8","Lua Crescente Minguante")

    )
    moon = models.CharField("Lua", max_length=1, choices=MOON)
    moon_day = models.PositiveIntegerField("Dia da Lua")
    
    def __str__(self):
        return self.campaign

class BattleChar(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.ForeignKey(Character, related_name="char_name", on_delete=models.CASCADE, blank=True, null=True)
    game = models.ForeignKey(Game, related_name="chars", on_delete=models.CASCADE)
    TYPE = (
        ("1","Aliados"),
        ("2","Inimigos")
    )
    type = models.CharField(max_length=1, choices=TYPE)
    temp_health = models.IntegerField()
    temp_rage = models.IntegerField()
    temp_gnosis = models.IntegerField()
    temp_will = models.IntegerField()
    dice = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        ordering = ("type", "name") 