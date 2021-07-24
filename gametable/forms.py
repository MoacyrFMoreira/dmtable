from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms

from .models import Game


class AddCharacter(forms.Form):
    pass

ATTR = (
    ("", "-"),
    ("strength", "Força"), 
    ("dextery", "Destreza"), 
    ("stamina", "Vigor"), 
    ("charisma", "Carisma"), 
    ("manipulation", "Manipulação"), 
    ("appearance", "Aparência"), 
    ("perception", "Percepção"), 
    ("intelligence", "Inteligência"), 
    ("wits", "Raciocínio")
)
HABL = (
    ("", "-"),
    ("alertness", "Prontidão"), 
    ("athletics", "Esportes"), 
    ("brawl", "Briga"), 
    ("empathy", "Empatia"), 
    ("expression", "Expressão"), 
    ("leadership", "Liderança"), 
    ("intimidation", "Intimidação"), 
    ("primal_urge", "Instinto Primitivo"), 
    ("streetwise", "Manha"), 
    ("subterfuge", "Lábia"), 
    ("animal_ken", "Empatia c/ Animais"), 
    ("crafts", "Ofícios"), 
    ("drive", "Condução"), 
    ("etiquette", "Etiqueta"), 
    ("firearms", "Armas de Fogo"), 
    ("larceny", "Crime"), 
    ("melee", "Armas Brancas"), 
    ("performance", "Performance"), 
    ("stealth", "Furitvidade"), 
    ("survival", "Sobrevivência"), 
    ("academics", "Acadêmicos"), 
    ("computer", "Computação"), 
    ("enigmas", "Enigmas"), 
    ("investigation", "Investigação"), 
    ("law", "Direito"), 
    ("medicine", "Medicina"), 
    ("occult", "Ocultismo"), 
    ("rituals", "Rituais"), 
    ("science", "Ciência"), 
    ("technology", "Tecnologia")
)
BKGR = (
    ("", "-"),
    ("allies", "Aliados"), 
    ("ancestors", "Ancestrais"), 
    ("contacts", "Contatos"), 
    ("fate", "Destino"), 
    ("fetish", "Feitiche"), 
    ("kinfolk", "Parentes"), 
    ("mentor", "Mentor"), 
    ("pure_breed", "Raça Pura"), 
    ("resources", "Recursos"), 
    ("rites", "Rituais"), 
    ("spirit_heritage", "Herança Espiritual"), 
    ("totem", "Totem"), 
    ("spirit_network", "Rede de Espíritos"), 
    ("prestige", "Prestígio"), 
    ("pack_status", "Status da Matilha")
)
class UpdateDices(forms.Form):
    attr = forms.ChoiceField(label="", choices=ATTR, required=False)
    habl = forms.ChoiceField(label="", choices=HABL, required=False)
    bkgr = forms.ChoiceField(label="", choices=BKGR, required=False)

class GameCreateForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            "campaign",
            "day",
            "time",
            "notes",
            "dm_only",
            "moon",
            "moon_day",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "."
        self.helper.add_input(
            Submit(
                "submit",
                "Atualizar",
                css_class="btn btn-success btn-lg btn-block",
            )
        )
        self.helper.layout = Layout(
            Fieldset(
                "",
                Field("campaign"),
                Div(
                    Field("notes", wrapper_class="col"),
                    Field("dm_only", wrapper_class="col"),
                    css_class="row",
                ),
                Div(
                    Field("day", wrapper_class="col"),
                    Field("time", wrapper_class="col"),
                    Field("moon", wrapper_class="col"),
                    Field("moon_day", wrapper_class="col"),
                    css_class="row",
                ),
                css_class="border-bottom mb-3",
            )
        )