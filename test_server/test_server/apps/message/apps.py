from django.apps import AppConfig


class MessageConfig(AppConfig):
    name = 'test_server.apps.message'
    def ready(self):
        import test_server.apps.message.signals.handler