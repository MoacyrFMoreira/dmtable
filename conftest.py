import pytest

from chars.tests.factories import GroupFactory, CharacterFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def group():
    return GroupFactory()


@pytest.fixture
def character():
    return CharacterFactory()
