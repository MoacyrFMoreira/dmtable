import pytest
from django.urls import resolve, reverse

from .factories import CharacterFactory

pytestmark = pytest.mark.django_db


class TestCharacterListView:
    def test_reverse_resolve(self):
        assert reverse("chars:list") == "/chars/"
        assert resolve("/chars/").view_name == "chars:list"

        url = reverse("chars:list_by_group", kwargs={"slug": "test-slug"})
        assert url == "/chars/group/test-slug/"

        view_name = resolve("/chars/group/test-slug/").view_name
        assert view_name == "chars:list_by_group"

    def test_status_code(self, client, group):
        response = client.get(reverse("chars:list"))
        assert response.status_code == 200

        response = client.get(
            reverse("chars:list_by_group", kwargs={"slug": group.slug})
        )
        assert response.status_code == 200


class TestCharacterDetailView:
    def test_reverse_resolve(self, character):
        url = reverse("chars:detail", kwargs={"slug": character.slug})
        assert url == f"/chars/{character.slug}/"

        view_name = resolve(f"/chars/{character.slug}/").view_name
        assert view_name == "chars:detail"

    def test_status_code(self, client):
        character = CharacterFactory(visible=True)
        url = reverse("chars:detail", kwargs={"slug": character.slug})
        response = client.get(url)
        assert response.status_code == 200