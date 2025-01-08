from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'

    def ready(self):
        # Import signals when the app is ready
        import contact.signals
