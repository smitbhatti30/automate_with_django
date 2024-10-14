import csv
from django.core.management.base import  BaseCommand
from django.apps import apps
import datetime

class Command(BaseCommand):
    help = 'Export data from Student model to a csv file'

    def add_arguments(self,parser):
        parser.add_argument('model_name',type = str, help= 'Model name')
                      
    def handle(self,*args,**kwargs):
        model_name = kwargs['model_name']

        model = None 
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label,model_name)
                break
            except LookupError:
                pass 

        if not model:
            self.stderr.write(f'Model {model_name} cound not found')
            return
        
        data = model.objects.all()

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-S")
        file_path = f'exported_{model_name}_data_{timestamp}.csv'
    
        with open(file_path,'w',newline='') as file:
            writer = csv.writer(file)

            writer.writerow([field.name for field in model._meta.fields])

            for dt in data:
                writer.writerow([getattr(dt,field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS('date Exported Successfully!'))