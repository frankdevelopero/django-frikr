from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from photos.views import home, detail
from users.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', home, name='photos_home'),
    path('photos/<int:pk>', detail, name='photos_detail'),

    path('login/', login, name='users_login'),
    path('logout/', logout, name='users_logout'),
]
