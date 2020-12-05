import pytest
from django.contrib.auth.models import User
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestModels:

    def test_user_create(self):
        User.objects.create_user('Amit', 'test@test.com')
        assert User.objects.count() == 1

    def test_extension(self):
        file = mixer.blend('file.File', file='test.pdf')
        assert file.extension() == 'pdf'

    def test_filename(self):
        file = mixer.blend('file.File', filename='test.pdf')
        assert file.__str__() == 'test.pdf'
