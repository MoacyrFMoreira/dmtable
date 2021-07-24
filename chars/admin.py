from django.contrib import admin

from .models import Archetype, Armor, Gift, Group, Character, Item, Merit, Rank, Rites, Type, Weapon

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "modified"]

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["name", "player", "breed", "tribe", "auspice", "rank", "race", "visible"]
    fieldsets = (
        (None, {"fields": ("group", "name", "short_name", "player", "image", "history", "visible", "race", "breed", "auspice", "tribe", "rank", "nature", "demeanor") }),
        ("Attributes", {"fields": [
            ("strength", "charisma", "perception"),
            ("dextery", "manipulation", "intelligence"),
            ("stamina", "appearance", "wits")
        ]}),
        ("Abilities", {"fields": [
            ("alertness", "animal_ken", "academics"),
            ("athletics", "crafts", "computer"),
            ("brawl", "drive", "enigmas"),
            ("empathy", "etiquette", "investigation"),
            ("expression", "firearms", "law"),
            ("leadership", "larceny", "medicine"),
            ("intimidation", "melee", "occult"),
            ("primal_urge", "performance", "rituals"),
            ("streetwise", "stealth", "science"),
            ("subterfuge", "survival", "technology")
        ]}),
        ("Traits", {"fields": (
            "rage", 
            "gnosis", 
            "willpower"
        )}),
        ("Backgrounds", {"fields": [
            ("allies", "ancestors", "contacts"),
            ("fate", "fetish", "kinfolk"),
            ("mentor", "pure_breed", "resources"),
            ("rites", "spirit_heritage", "totem"),
            ("spirit_network", "prestige", "pack_status")
        ]}),
        ("Gifts & Rites", {"fields": [("gifts",),("rite_list",)]}),
        ("Merits & Flaws", {"fields": ("merits",)}),
        ("Itens", {"fields": ("weapons","armors","itens")}),
    )
    list_filter = ["group", "visible", "breed", "auspice", "tribe", "race"]
    list_editable = ["visible"]
    filter_horizontal = ("gifts","rite_list", "merits","weapons","armors","itens")

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "classfication", "initial_bonus", "initial_optional"]

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ["rank", "initial_gift", "bonus"]

@admin.register(Archetype)
class ArchetypeAdmin(admin.ModelAdmin):
    list_display = ["name", "willpower_condition"]

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "level"]
    list_filter = ["type",]

@admin.register(Rites)
class RitesAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "level"]
    list_filter = ["type",]

@admin.register(Merit)
class MeritAdmin(admin.ModelAdmin):
    list_display = ["name", "cost"]

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ["name", "dificulty", "damage", "description"]

@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    list_display = ["name", "armor", "description"]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]