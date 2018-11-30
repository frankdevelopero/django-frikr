from django.urls import path
from photos.views import HomeView, PhotoListView, PhotoDetailView, CreateView,  UserPhotosView
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('', HomeView.as_view(), name='photos_home'),
    path('photos/<int:pk>', PhotoDetailView.as_view(), name='photos_detail'),
    path('photos/new/', CreateView.as_view(), name='create_photo'),
    path('photos/', PhotoListView.as_view(), name='photos_list'),
    path('my-photos/', login_required(UserPhotosView.as_view()), name='user_photos'),


]
