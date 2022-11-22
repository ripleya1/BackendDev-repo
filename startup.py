from os import system
import platform
import subprocess

def startServer():
    makeMigrationsProc = subprocess.Popen(["python", "manage.py", "makemigrations"], shell=True)
    makeMigrationsProc.wait()
    migrateProc = subprocess.Popen(["python", "manage.py", "migrate"], shell=True)
    migrateProc.wait()
    runserverProcess = subprocess.Popen(["python", "manage.py" ,"runserver"], shell=True)
    return(runserverProcess)

def stopServer(runServerProcess):
    runServerProcess.terminate()
    # try:
    #     if(platform.system() == "Windows"):
    #             system("del databases/db.sqlite3")
    #     else:
    #             system("rm databases/db.sqlite3")
    # except Exception as e:
    #     print("Exception: " + e)

proc = startServer()
stopServer(proc)