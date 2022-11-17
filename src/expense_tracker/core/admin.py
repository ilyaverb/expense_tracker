from django.contrib import admin
from django.apps import apps
# from api.core.models import Transaction, Category

admin.site.register(apps.get_app_config('core').get_models())
