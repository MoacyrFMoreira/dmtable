import copy, random

from chars.models import Character
from .models import BattleChar, Game

class Campaign:
    def __init__(self, request):
        if request.session.get("game") is None:
            request.session["game"] = {}
            if BattleChar.objects.exists():
                game_id = Game.objects.first().id
                chars = BattleChar.objects.filter(game=game_id)
                for char in chars:
                    request.session["game"][str(char.id)] = {
                        "quantity": 0,
                        "type":"1",
                        "dices":0,
                    }
                    request.session["game"][str(char.id)]["quantity"] = 1
                    request.session["game"][str(char.id)]["type"] = int(char.type)
                    request.session["game"][str(char.id)]["dices"] = char.dice
        self.game = request.session["game"]
        self.session = request.session

    def __iter__(self):
        game = copy.deepcopy(self.game)
        chars = Character.objects.filter(id__in=game)

        for char in chars:
            game[str(char.id)]["char"] = char
        for item in game.values():
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.game.values())

    def add(self, char, type=1):
        character_id = str(char.id)
        if character_id not in self.game:
            self.game[character_id] = {
                "quantity": 0,
                "type":"1",
                "dices":0,
            }
        self.game[character_id]["quantity"] = 1
        self.game[character_id]["type"] = type
        self.save()

    def remove(self, char):
        character_id = str(char.id)

        if character_id in self.game:
            del self.game[character_id]
            self.save()

    def clear(self):
        del self.session["game"]
        self.save()
    
    def dices(self, attr, habl, bkgr):
        chars = Character.objects.filter(id__in=self.game)
        for char in chars:
            dice = 0
            if attr != "":
                dice += char.__getattribute__(attr)
            if habl != "":
                dice += char.__getattribute__(habl)
            if bkgr != "":
                dice += char.__getattribute__(bkgr)
            
            BattleChar.objects.filter(id=str(char.id)).update(dice=dice)
            self.game[str(char.id)]["dices"] = dice
        self.save()

    def save(self):
        self.session.modified = True

class Table:
    def get_game():
        table = Game.objects.first()
        return table

    def rolldices(dices):
        x = ""
        for d in range(0, dices):
            r = random.randint(1, 10)
            x += str(r)
            if d < (dices-1):
                x += ", "
        return x

    def update_roll(character_id, dices):
        table = Table.get_game()
        char = Character.objects.get(id=str(character_id))
        new_text = ""
        if dices > 0:
            new_text = char.name + " rolou " + str(dices) + " dados: (" + Table.rolldices(dices) + ")\n"
        textlines = table.rolls.splitlines()
        text = "\n".join(textlines[:10])
        new_text = new_text + text
        Game.objects.filter(id=table.id).update(rolls=new_text)
        table = Table.get_game()
        return table