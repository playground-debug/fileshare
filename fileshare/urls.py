from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from file import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('accounts/', include('account.urls'), name='accounts'),
    path('file/', include('file.urls'), name='files')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
