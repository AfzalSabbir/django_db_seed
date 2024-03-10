from django.core.management.base import BaseCommand

from django_db_seed.helpers import backup, restore


class Command(BaseCommand):
    help = 'This command will backup/restore the database.'

    def add_arguments(self, parser):
        # Add a positional argument
        parser.add_argument('--mode', type=str, help='Mode: backup or restore')

    def handle(self, *args, **options):
        mode = options['mode']

        if mode == 'backup' or mode == 'create' or mode is None:
            backup()
        elif mode == 'restore' or mode == 'load':
            restore()
        else:
            self.stdout.write(self.style.ERROR('Invalid mode!'))
