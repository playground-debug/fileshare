from django.test import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse, resolve
from mixer.backend.django import mixer
from file.views import uploadfile, portal, homepage
import pytest
from django.test import TestCase


@pytest.mark.django_db
class TestViews(TestCase):

    def test_homepage_succeess(self):
        path = reverse('homepage')
        request = RequestFactory().get(path)

        response = self.client.get(path)
        assert response.status_code == 200

    def test_uploadfile_authenticated(self):
        path = reverse('uploadfile')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = uploadfile(request)
        assert response.status_code == 200

    def test_uploadfile_unauthenticated(self):
        path = reverse('uploadfile')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()

        response = uploadfile(request)
        assert 'accounts/login' in response.url

    def test_portal_succeess(self):
        path = reverse('portal')
        request = RequestFactory().get(path)

        response = portal(request)
        assert response.status_code == 200
