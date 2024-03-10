import json
import os

from django.apps import apps
from django.core.management import call_command
from django.core.serializers import serialize
from django.conf import settings

default_db_seed = {
    'seed_dir': f"{settings.BASE_DIR}/db_seed/",
    'apps': [
        "admin",
        "auth",
    ]
}

db_seed = getattr(
    settings,
    'DJANGO_DB_SEED',
    default_db_seed
)

db_seed_dir = db_seed.get('seed_dir', default_db_seed['seed_dir'])
db_seed_apps = db_seed.get('apps', default_db_seed['apps'])


def get_models():
    """
    Get a list of all models in the database
    """

    models = {}

    # include only these apps to back up their data
    app_names = db_seed_apps

    # Get a list of all installed apps
    installed_apps = apps.get_app_configs()

    # Iterate over each app and list its models
    for app in installed_apps:
        if app.label not in models:
            _models = app.get_models()

            if app.label not in app_names:
                continue

            models[app.label] = []
            for model in _models:
                models[app.label].append(f"{model._meta.object_name}")

    return models


def backup():
    """
    Backup data from the database
    """

    models = get_models()

    # loop over models
    for app in models:
        print(f"App: {app}")
        ensure_directory_exists(db_seed_dir + app)
        for model in models[app]:
            print(f" - {model}")
            # get the model's data
            model_class = apps.get_model(app, model)
            model_data = model_class.objects.all()

            print(f"   - backing up {model}...")

            # dumpdata
            dump_model_data_to_json(f"{app}.{model}", f"{db_seed_dir}{app}/{model}.json")


def restore():
    """
    Restore data from a backup
    """
    models = get_models()

    # loop over models
    for app in models:
        print(f"\n\rApp: {app}")
        for model in models[app]:
            print(f" - {model}")
            # restore the model
            print(f"   - restoring {model}...")
            # restore the model
            model_class = apps.get_model(app, model)
            truncate_data(model_class)

            # loaddata
            load_data_from_json(f"{db_seed_dir}{app}/{model}.json")


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def dump_model_data_to_json_stringify(model_name, output_file):
    # Call Django's dumpdata management command to dump data from the specified model
    with open(output_file, 'w') as f:
        call_command('dumpdata', model_name, stdout=f)


def dump_model_data_to_json(model_name, output_file, indent=4):
    # Get the model class dynamically
    model_class = apps.get_model(model_name)

    # Query data from the model
    queryset = model_class.objects.all()

    # Serialize queryset to JSON
    serialized_data = serialize('json', queryset)

    # Load serialized data
    loaded_data = json.loads(serialized_data)

    # Write the JSON data to a file
    with open(output_file, 'w') as f:
        json.dump(loaded_data, f, indent=indent)


def load_data_from_json(input_file):
    # Call Django's loaddata management command to load data from the specified JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
        call_command('loaddata', input_file)


def truncate_data(model_class):
    # Truncate existing data in the model
    model_class.objects.all().delete()

    # Your restoration logic here
    # For example, you can load data from a JSON file and create model instances
    # After truncating, you can seed data or load data from a file
    # Example: data = [...] and then create instances

    print('Truncated data from the model:', model_class)
