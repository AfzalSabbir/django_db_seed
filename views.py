from pathlib import Path

from django.shortcuts import render
from django.apps import apps

from django_db_seed import helpers


# Create your views here.


def backup(request):
    """
    Backup data from the database
    """

    helpers.backup()

    context = {
        "title": "Backup done!"
    }

    return render(request, "django_db_seed/backup.html", context)


def restore(request):
    """
    Restore data from a backup
    """

    helpers.restore()

    context = {
        "title": "Restore done!"
    }

    return render(request, "django_db_seed/restore.html", context)
