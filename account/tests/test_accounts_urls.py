from django.urls import reverse, resolve


class TestAccountsUrls:

    def test_signup_url(self):
        path = reverse('signup')
        assert resolve(path).route == 'accounts/signup'

    def test_login_url(self):
        path = reverse('login')
        assert resolve(path).route == 'accounts/login'

    def test_logout_url(self):
        path = reverse('logout')
        assert resolve(path).route == 'accounts/logout'

    def test_homepage_url(self):
        path = reverse('homepage')
        assert resolve(path).route == ''
