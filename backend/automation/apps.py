from django.apps import AppConfig


class AutomationConfig(AppConfig):
    name = 'automation'
    
    def ready(self): 
        print("Automation Initialized")