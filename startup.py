from os import system
import platform

def startServer():
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