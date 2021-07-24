from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from users.models import User


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(visible=True)


class Group(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    TIPO = (
        ("1","Caern"), 
        ("2","Matilha"), 
        ("3","Outro")
    )
    type = models.CharField(max_length=1, choices=TIPO)
    totem = models.CharField(max_length=255, unique=True, null=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "group"
        verbose_name_plural = "groups"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("chars:list_by_group", kwargs={"slug": self.slug})

class Type(models.Model):
    name = models.CharField(max_length=255)
    CLASSF = (
        ("1","Race"), 
        ("2","Breed"), 
        ("3","Auspice"),
        ("4","Tribe")
    )
    classfication = models.CharField(max_length=2, choices=CLASSF)
    initial_bonus = models.PositiveIntegerField()
    initial_optional = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ("initial_bonus",)

class Rank(models.Model):
    rank = models.CharField(max_length=255, unique=True)
    initial_gift = models.PositiveIntegerField()
    bonus = models.IntegerField()

    def __str__(self):
        return self.rank

    class Meta:
        ordering = ("bonus",)

class Gift(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    level = models.PositiveIntegerField(default=1)
    spirit_type = models.CharField(max_length=255, blank=True)
    test = models.CharField(max_length=255, blank=True)
    cost = models.CharField(max_length=255, blank=True)
    time = models.CharField(max_length=255, blank=True)
    duration = models.CharField(max_length=255, blank=True)
    effect = models.TextField(blank=True)
    refference = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name + " (Nv." + str(self.level) + " " + str(self.type) + ")"

    class Meta:
        ordering = ("name",)

class Rites(models.Model):
    name = models.CharField(max_length=255)
    level = models.PositiveIntegerField(default=1)
    RITE_TYPE = (
        ("1","Menor"),
        ("2","Caern"),
        ("3","Místico"),
        ("4","Morte"),
        ("5","Pacto"),
        ("6","Periódico"),
        ("7","Punição"),
        ("8","Renome")
    )
    type = models.CharField(max_length=2, choices=RITE_TYPE, default="1")
    system = models.TextField(blank=True)
    effect = models.TextField(blank=True)

    def __str__(self):
        return self.name + " (Nv." + str(self.level) + ")"

    class Meta:
        ordering = ("name",)

class Archetype(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    willpower_condition = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("name",)

class Merit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    cost = models.IntegerField(default=0, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name + " - " + str(self.cost)

    class Meta:
        ordering = ("name",)

class Weapon(models.Model):
    name = models.CharField(max_length=255, unique=True)
    dificulty = models.PositiveIntegerField(default=6)
    damage = models.CharField(max_length=10)
    range = models.CharField(max_length=10, blank=True)
    bullets = models.CharField(max_length=10, blank=True)
    stealth = models.CharField(max_length=20, blank=True)
    ATTB = (
        ("brawl","Briga"),
        ("melee","Armas Brancas"),
        ("firearms","Armas de Fogo"),
        ("athletics","Esportes")
    )
    attribute = models.CharField(max_length=10, choices=ATTB, default="brawl")
    DMG = (
        ("1","Contusão"),
        ("2","Letal"),
        ("3","Agravado")
    )
    damage_type = models.CharField(max_length=1, choices=DMG, default="2")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("name",)
    
class Armor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    armor = models.IntegerField(default=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name + " + " + str(self.armor)
    
    class Meta:
        ordering = ("name",)

class Item(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("name",)

class Character(TimeStampedModel):
    group = models.ForeignKey(Group, related_name="group", null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=12, blank=True)
    player = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="chars", blank=True)
    history = models.TextField(blank=True)
    visible = models.BooleanField(default=True)
    rank = models.ForeignKey(Rank, blank=True, null=True, on_delete=models.SET_NULL)
    race = models.ForeignKey(Type, limit_choices_to={"classfication": "1"}, related_name="char_race", blank=True, null=True, on_delete=models.SET_NULL)
    breed = models.ForeignKey(Type, limit_choices_to={"classfication": "2"}, related_name="char_breed", blank=True, null=True, on_delete=models.SET_NULL)
    auspice = models.ForeignKey(Type, limit_choices_to={"classfication": "3"}, related_name="char_auspice", blank=True, null=True, on_delete=models.SET_NULL)
    tribe = models.ForeignKey(Type, limit_choices_to={"classfication": "4"}, related_name="char_tribe", blank=True, null=True, on_delete=models.SET_NULL)
    nature = models.ForeignKey(Archetype, blank=True, null=True, on_delete=models.SET_NULL, related_name="nature")
    demeanor = models.ForeignKey(Archetype, blank=True, null=True, on_delete=models.SET_NULL, related_name="demeanor")

    health = models.IntegerField(default=7)
    rage = models.PositiveIntegerField(default=0)
    gnosis = models.PositiveIntegerField(default=0)
    willpower = models.PositiveIntegerField(default=1)
# atribbutes
    strength = models.PositiveIntegerField(default=1)
    dextery = models.PositiveIntegerField(default=1)
    stamina = models.PositiveIntegerField(default=1)
    charisma = models.PositiveIntegerField(default=1)
    manipulation = models.PositiveIntegerField(default=1)
    appearance = models.PositiveIntegerField(default=1)
    perception = models.PositiveIntegerField(default=1)
    intelligence = models.PositiveIntegerField(default=1)
    wits = models.PositiveIntegerField(default=1)
# abilities
    alertness = models.PositiveIntegerField(default=0)
    athletics = models.PositiveIntegerField(default=0)
    brawl = models.PositiveIntegerField(default=0)
    empathy = models.PositiveIntegerField(default=0)
    expression = models.PositiveIntegerField(default=0)
    leadership = models.PositiveIntegerField(default=0)
    intimidation = models.PositiveIntegerField(default=0)
    primal_urge = models.PositiveIntegerField(default=0)
    streetwise = models.PositiveIntegerField(default=0)
    subterfuge = models.PositiveIntegerField(default=0)
    animal_ken = models.PositiveIntegerField(default=0)
    crafts = models.PositiveIntegerField(default=0)
    drive = models.PositiveIntegerField(default=0)
    etiquette = models.PositiveIntegerField(default=0)
    firearms = models.PositiveIntegerField(default=0)
    larceny = models.PositiveIntegerField(default=0)
    melee = models.PositiveIntegerField(default=0)
    performance = models.PositiveIntegerField(default=0)
    stealth = models.PositiveIntegerField(default=0)
    survival = models.PositiveIntegerField(default=0)
    academics = models.PositiveIntegerField(default=0)
    computer = models.PositiveIntegerField(default=0)
    enigmas = models.PositiveIntegerField(default=0)
    investigation = models.PositiveIntegerField(default=0)
    law = models.PositiveIntegerField(default=0)
    medicine = models.PositiveIntegerField(default=0)
    occult = models.PositiveIntegerField(default=0)
    rituals = models.PositiveIntegerField(default=0)
    science = models.PositiveIntegerField(default=0)
    technology = models.PositiveIntegerField(default=0)
# backgrounds
    allies = models.PositiveIntegerField(default=0)
    ancestors = models.PositiveIntegerField(default=0)
    contacts = models.PositiveIntegerField(default=0)
    fate = models.PositiveIntegerField(default=0)
    fetish = models.PositiveIntegerField(default=0)
    kinfolk = models.PositiveIntegerField(default=0)
    mentor = models.PositiveIntegerField(default=0)
    pure_breed = models.PositiveIntegerField(default=0)
    resources = models.PositiveIntegerField(default=0)
    rites = models.PositiveIntegerField(default=0)
    spirit_heritage = models.PositiveIntegerField(default=0)
    totem = models.PositiveIntegerField(default=0)
    spirit_network = models.PositiveIntegerField(default=0)
    prestige = models.PositiveIntegerField(default=0)
    pack_status = models.PositiveIntegerField(default=0)
#ManyToMany
    gifts = models.ManyToManyField(Gift, blank=True)
    rite_list = models.ManyToManyField(Rites, blank=True)
    merits = models.ManyToManyField(Merit, blank=True)
    weapons = models.ManyToManyField(Weapon, blank=True)
    armors = models.ManyToManyField(Armor, blank=True)
    itens = models.ManyToManyField(Item, blank=True)
#auxiliary fields
    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("chars:detail", kwargs={"slug": self.slug})