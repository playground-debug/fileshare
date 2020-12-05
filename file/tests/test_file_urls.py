from django.urls import reverse, resolve


class TestFileUrls:

    def test_uploadFile_url(self):
        path = reverse('uploadfile')
        assert resolve(path).view_name == 'uploadfile'

    def test_portal_url(self):
        path = reverse('portal')
        assert resolve(path).view_name == 'portal'
