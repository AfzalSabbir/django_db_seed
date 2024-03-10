from django.urls import path

from .views import backup, restore

urlpatterns = [
    path('', backup, name='backups'),
    path('restore/', restore, name='restores')
]
