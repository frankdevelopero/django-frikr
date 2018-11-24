from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from photos.views import home, detail, create
from users.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', home, name='photos_home'),
    path('photos/<int:pk>', detail, name='photos_detail'),
    path('photos/new/', create, name='create_photo'),

    path('login/', login, name='users_login'),
    path('logout/', logout, name='users_logout'),
]
