from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse
from django.views.decorators.http import require_POST
from django.views.generic import CreateView

from chars.models import Character

from .forms import GameCreateForm, AddCharacter, UpdateDices
from .game import Campaign, Table
from .models import Game, BattleChar


@require_POST
def game_add(request, character_id):
    game = Campaign(request)
    char = get_object_or_404(Character, id=character_id)
    form = AddCharacter(request.POST)
    if form.is_valid():
        game.add(char)

    return redirect("gametable:detail")

@require_POST
def game_update(request, character_id, type):
    game = Campaign(request)
    char = get_object_or_404(Character, id=character_id)
    form = AddCharacter(request.POST)
    if form.is_valid():
        if type == "1":
            game.add(char, 2)
            if BattleChar.objects.filter(id=character_id).exists():
                BattleChar.objects.filter(id=character_id).update(type=2)
        elif type == "2":
            game.add(char, 1)
            if BattleChar.objects.filter(id=character_id).exists():
                BattleChar.objects.filter(id=character_id).update(type=1)
    return redirect("gametable:detail")

@require_POST
def game_remove(request, character_id):
    game = Campaign(request)
    char = get_object_or_404(Character, id=character_id)
    game.remove(char)
    if BattleChar.objects.filter(id=character_id).exists():
        BattleChar.objects.filter(id=character_id).delete()
    return redirect("gametable:detail")

def game_detail(request):
    game = Campaign(request)
    return render(request, "gametable/game_detail.html", {"game": game})

def game_home(request):
    game = Campaign(request)
    game.clear()
    game = Campaign(request)
    table = Table.get_game()
    form = UpdateDices()
    return render(request, "gametable/game_table.html", {"game": game, "table":table, "form":form})

@require_POST
def update_dices(request):
#   Calcula os Dados do Teste
    game = Campaign(request)
    attr = request.POST["attr"]
    habl = request.POST["habl"]
    bkgr = request.POST["bkgr"]
    game.dices(attr, habl, bkgr)
    table = Table.get_game()
    form = UpdateDices(request.POST)
    return render(request, "gametable/game_table.html", {"game": game, "table":table, "form":form})

@require_POST
def roll_dices(request, character_id, dices):
    game = Campaign(request)
    table = Table.update_roll(character_id, dices)
    form = UpdateDices(request.POST)
    return render(request, "gametable/game_table.html", {"game": game, "table":table, "form":form})

class GameCreateView(CreateView):
    model = Game
    form_class = GameCreateForm

    def form_valid(self, form):
        game = Campaign(self.request)
        if game:
            if Game.objects.exists():
                id = Game.objects.first().id
                record = Game.objects.get(id=id)
                form = GameCreateForm(self.request.POST, instance=record)
            campaign = form.save()
            for item in game:
                if BattleChar.objects.filter(id=item["char"].id).exists() == False:
                    BattleChar.objects.create(
                        id = item["char"].id,
                        game=campaign,
                        name=item["char"],
                        type=item["type"],
                        temp_health=item["char"].health,
                        temp_rage=item["char"].rage,
                        temp_gnosis=item["char"].gnosis,
                        temp_will=item["char"].willpower,
                    )
        return HttpResponseRedirect(reverse("gametable:table"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Game.objects.exists():
            id = Game.objects.first().id
            record = Game.objects.get(id=id)
            form = GameCreateForm(instance=record)
            context = {'form':form}
        context["game"] = Campaign(self.request)
        return context