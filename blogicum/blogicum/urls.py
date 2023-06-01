
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('blog.urls')),
    path('posts/<int:id>/', include('blog.urls')),
    path('category/<slug:category_slug>/', include('blog.urls')),
    path('pages/', include('pages.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
