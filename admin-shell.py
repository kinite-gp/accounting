import readline
from os import system
from colorama import Fore, init


init()



addrs = ['runserver',
         'createsuperuser',
         "check",
         "compilemessages",
         "createcachetable",
         "dbshell",
         "diffsettings",
         "dumpdata",
         "flush",
         "inspectdb",
         "loaddata",
         "makemessages",
         "makemigrations",
         "migrate",
         "optimizemigration",
         "shell",
         "showmigrations",
         "sqlflush",
         "sqlmigrate",
         "sqlsequencereset",
         "squashmigrations",
         "startapp",
         "startproject",
         "test",
         "testserver",
         "collectstatic",
         "findstatic",
         "clearsessions",
         "changepassword",
         "remove_stale_contenttypes",
         "django-admin startproject",
         "exit",
         ]

            

def completer(text, state):
    options = [x for x in addrs if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None


readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

while 1:
    try:
        command = input(Fore.BLUE + "python manage.py ")
        if command == "exit":
            exit("exit admin shell")
        elif command == "help":
            for a in addrs:
                print(a)
        elif "django-admin startproject" in command:
            system(command)
        else:
            
            print(' ' + Fore.RESET)
            system(f"python-django manage.py {command}")
            
    except KeyboardInterrupt:
        print("\nKeyboard interrupted !!!\n")
        