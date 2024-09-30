from django.core.management.base import BaseCommand


#Proposed Command = python manage.py greeting Name
#Proposed output = Hi {name}, Good Morning
class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser):
        parser.add_argument('name',type=str,help='Specifies user name')

    def handle(self,*args,**kwargs):
        #write the logic 
        name = kwargs['name']
        greeting = f'Hi {name},Good Morning!'
        # self.stdout.write(greeting)
        # self.stderr.write(greeting)
        self.stderr.write(self.style.SUCCESS(greeting))
        # self.stderr.write(self.style.WARNING(greeting))