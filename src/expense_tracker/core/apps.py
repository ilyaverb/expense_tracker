from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expense_tracker.core'
    label = 'core'

    def ready(self):
        import expense_tracker.core.signals
