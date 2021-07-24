from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Armor, Group, Character, Gift, Item, Merit, Rites, Weapon

from gametable.forms import AddCharacter


class CharDetailView(DetailView):
    queryset = Character.available.all()
    extra_context = {"form": AddCharacter()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gift"] = Gift.objects.all()
        context["rite_list"] = Rites.objects.all()
        context["merits"] = Merit.objects.all()
        context["weapons"] = Weapon.objects.all()
        context["armors"] = Armor.objects.all()
        context["itens"] = Item.objects.all()    
        return context


class CharListView(ListView):
    group = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Character.available.all() 

        group_slug = self.kwargs.get("slug")
        if group_slug:
            self.group = get_object_or_404(Group, slug=group_slug)
            queryset = queryset.filter(group=self.group)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["group"] = self.group
        context["groups"] = Group.objects.all()
        return context