import pytest
from pytest_django.asserts import assertQuerysetEqual

from ..models import Character
from .factories import CharacterFactory

pytestmark = pytest.mark.django_db


class TestGroupModel:
    def test___str__(self, group):
        assert group.__str__() == group.name
        assert str(group) == group.name

    def test_get_absolute_url(self, group):
        url = group.get_absolute_url()
        assert url == f"/chars/group/{group.slug}/"


class TestCharacterModel:
    def test___str__(self, character):
        assert character.__str__() == character.name
        assert str(character) == character.name

    def test_get_absolute_url(self, character):
        url = character.get_absolute_url()
        assert url == f"/chars/{character.slug}/"

    def test_available_manager(self):
        CharacterFactory(visible=True)
        CharacterFactory(visible=False)

        assert Character.objects.count() == 2
        assert Character.available.count() == 1
        assertQuerysetEqual(
            Character.available.all(),
            Character.objects.filter(visible=True),
            transform=lambda x: x,
        )