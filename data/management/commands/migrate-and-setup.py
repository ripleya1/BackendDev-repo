from django.core.management.base import BaseCommand, CommandError
import subprocess

class Command(BaseCommand):
    help = 'Initialize databases with authenticated users for access'

    def add_arguments(self, parser):
        parser.add_argument("-t", "--testing", action="store_true", help="Runs the script as it is intended to be used for automated testing.")
        parser.add_argument("-s", "--runserver", action="store_true", help="Runs the server.")
    
    def handle(self, *args, **kwargs):
        if kwargs["testing"]:
            makeMigrationsProc = subprocess.Popen(["python", "manage.py", "makemigrations", "data"], shell=True)
            makeMigrationsProc.wait()
            migrateProc = subprocess.Popen(["python", "manage.py", "migrate", "--database=testing"], shell=True)
            migrateProc.wait()
            db_startupProc = subprocess.Popen(["python", "manage.py", "db_startup", "--settings=BackendDev.testSettings"], shell=True)
            db_startupProc.wait()
            
        else:
            makeMigrationsProc = subprocess.Popen(["python", "manage.py", "makemigrations", "data"], shell=True)
            makeMigrationsProc.wait()
            migrateProc = subprocess.Popen(["python", "manage.py", "migrate"], shell=True)
            migrateProc.wait()
            db_startupProc = subprocess.Popen(["python", "manage.py", "db_startup"], shell=True)
            db_startupProc.wait()