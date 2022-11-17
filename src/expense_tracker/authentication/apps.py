from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expense_tracker.authentication'
    label = 'authentication'

    def ready(self):
        import expense_tracker.authentication.signals
