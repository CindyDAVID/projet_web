from django.contrib import admin
from django.urls import path, include
from Event import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/', include('Event.urls')),
]
