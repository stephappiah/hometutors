from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # Add this to use signals
    def ready(self):
        from . import signals 
