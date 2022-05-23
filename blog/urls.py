from django.conf import settings # added to handle images
from django.conf.urls.static import static # added to handle images
from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'), # Here TAKE CARE OF THE ORDER → THIS IS CORRECT ✓ ✓ ✓
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # added to handle images