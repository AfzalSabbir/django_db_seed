# Django DB Seed

Django DB Seed is a Django package designed to simplify the process of seeding your database with initial data. It provides a convenient way to define and load seed data into your Django project.

## Installation

You can install Django DB Seed using pip:

```bash
pip install django-db-seed
```

## Configuration

To configure Django DB Seed, you can define the following settings in your Django project's settings file (`settings.py`):

```python
# settings.py

# ...

INSTALLED_APPS = (
    # ...
    'django_db_seed',
)

# ...

DJANGO_DB_SEED = {
    'seed_dir': "db-seed/",
    'apps': [
        "admin",
        "auth",
        # ...
    ]
}

# ...
```

- `seed_dir`: Specifies the directory where your seed data files are located. By default, it is set to a directory named `db-seed` in your project's base directory (`BASE_DIR`).
- `apps`: Specifies the Django apps for which you want to load seed data. You can specify one or more app names in a list.

## Usage

Once configured, you can use Django DB Seed to manage your database seed data.

### Backup Database Seed Data

To backup the seed data in your files, run the following management command:

```bash
python manage.py db-seed --mode=backup
```

### Restore Database Seed Data

To restore the seed data in your database from backup, run the following management command:

```bash
python manage.py db-seed --mode=restore
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
