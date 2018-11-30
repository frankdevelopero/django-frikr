from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from photos.views import HomeView, PhotoListView, PhotoDetailView, CreateView,  UserPhotosView
from users.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', HomeView.as_view(), name='photos_home'),
    path('photos/<int:pk>', PhotoDetailView.as_view(), name='photos_detail'),
    path('photos/new/', CreateView.as_view(), name='create_photo'),
    path('photos/', PhotoListView.as_view(), name='photos_list'),
    path('my-photos/', login_required(UserPhotosView.as_view()), name='user_photos'),
    path('login/', LoginView.as_view(), name='users_login'),
    path('logout/', LogoutView.as_view(), name='users_logout'),
]
