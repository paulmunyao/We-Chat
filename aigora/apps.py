from django.apps import AppConfig


class AigoraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aigora'

    def ready(self):
        import aigora.signals 


