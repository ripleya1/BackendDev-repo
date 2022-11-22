from os import system
import platform
import subprocess

def startServer():
    migrateProc = subprocess.Popen(["python", "manage.py", "migrate"], shell=True)
    migrateProc.wait()
    # global runserverProcess 
    runserverProcess = subprocess.Popen(["python", "manage.py" ,"runserver"], shell=True)
    # yield(runserverProcess)
    yield
    runserverProcess.terminate()

    try:
        if(platform.system() == "Windows"):
            system("del databases/db.sqlite3")
        else:
            system("rm databases/db.sqlite3")
    except Exception as e:
        print("Exception: " + e)

    system("python manage.py makemigrations")
    system("python manage.py migrate")
    system("python manage.py runserver")

startServer()