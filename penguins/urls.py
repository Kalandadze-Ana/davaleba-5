from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('penguin/kawasaki/', include('kawasaki.urls')),
    path('penguin/kago/', include('kago.urls')),
    path('penguin/krico/', include('krico.urls')),
    path('penguin/estriper/', include('estriper.urls')),
]