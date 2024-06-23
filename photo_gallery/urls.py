# photo_gallery/urls.py
from django.urls import path
from .views import PhotoListView, PhotoDetailView, like_photo, register, login_view, profile

urlpatterns = [
    path('', PhotoListView.as_view(), name='home'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('like/<int:photo_id>/', like_photo, name='like_photo'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
]
