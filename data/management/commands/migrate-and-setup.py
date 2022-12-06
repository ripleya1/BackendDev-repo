from django.core.management.base import BaseCommand, CommandError
import subprocess
import platform

class Command(BaseCommand):
    help = 'Initialize databases with authenticated users for access'

    def add_arguments(self, parser):
        parser.add_argument("-t", "--testing", action="store_true", help="Runs the script as it is intended to be used for automated testing.")
    
    def handle(self, *args, **kwargs):
        if platform.system() == "Windows":
            shellFlag = True
        else:
            shellFlag = False
        if kwargs["testing"]:
            makeMigrationsProc = subprocess.Popen(["python", "manage.py", "makemigrations", "data"], shell=shellFlag)
            makeMigrationsProc.wait()
            migrateProc = subprocess.Popen(["python", "manage.py", "migrate", "--database=testing"], shell=shellFlag)
            migrateProc.wait()
            db_startupProc = subprocess.Popen(["python", "manage.py", "db_startup", "--settings=BackendDev.testSettings"], shell=shellFlag)
            db_startupProc.wait()
            
        else:
            makeMigrationsProc = subprocess.Popen(["python", "manage.py", "makemigrations", "data"], shell=shellFlag)
            makeMigrationsProc.wait()
            migrateProc = subprocess.Popen(["python", "manage.py", "migrate"], shell=shellFlag)
            migrateProc.wait()
            db_startupProc = subprocess.Popen(["python", "manage.py", "db_startup"], shell=shellFlag)
            db_startupProc.wait()