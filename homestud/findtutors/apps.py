from django.apps import AppConfig


class FindtutorsConfig(AppConfig):
    name = 'findtutors'

    # Add this to use signals
    def ready(self):
        from . import signals 