from django.apps import AppConfig


class Corona3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Corona3'
    
    # def ready(self): #method just to import the signals
    # 	import Patient.signals
