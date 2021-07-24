import factory
import factory.fuzzy

from ..models import Group, Character


class GroupFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    type = factory.fuzzy.FuzzyChoice("1,2,3")

    class Meta:
        model = Group


class CharacterFactory(factory.django.DjangoModelFactory):
    group = factory.SubFactory(GroupFactory)
    name = factory.fuzzy.FuzzyText()
    image = factory.django.ImageField()
    history = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)
    health = factory.fuzzy.FuzzyInteger(1, 999)
    visible = factory.Faker("pybool")

    class Meta:
        model = Character