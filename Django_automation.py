""" This python file helps to make full flushed Django Project, Django Apps, static and templates directories."""
choice = int(input("1 -> Creating a new project\n2 -> Looking for changes in models.py\n"))
import os
os.system('cmd /c python -m pip install django webbrowser')
import webbrowser
import time
from sys import platform

if choice == 1:
    print("Please do not use space in your project/app name at the end!")
    project_name = str(input("Whats your project name : ")).capitalize()
    apps_name = str(input("What your apps name : ")).split(",")
    want_env = str(input("Do you want to create a virtual environment? (y/n) : ")).capitalize()


    # check if the project name is in the current directory
    if os.path.isdir(project_name):
        print("Project name is already in the current directory")
        cmd_delete = str(input("Would you like to delete it? (y/n) : "))
        if cmd_delete == "y":
            os.system("rmdir /S " + project_name)
            print("Project deleted!And New project is being created")
            os.system('cmd /c "django-admin startproject ' + project_name)
            # change the directory to the project name
            os.chdir(project_name)
            if os.path.isdir(apps_name[0].capitalize()):
                print("Apps name is already in the project directory")
                exit()
            else:
                # check if apps_name has more than one app
                if len(apps_name) > 1:
                    for app in apps_name:
                        os.system('cmd /c "django-admin startapp ' + app.capitalize())
                    if want_env == "Y":
                        os.system('cmd /c "pip install virtualenv"')
                        os.system('cmd /c "virtualenv env"')
                        os.chdir("env")
                        os.chdir("Scripts")
                        # Check the Operating system and start the virtualenv
                        #------------Not working on Windows 10-------------
                        if platform == "linux" or platform == "linux2":#Linux
                            os.system('cmd /c "source activate"')
                        elif platform == "darwin":#MAC OS
                            os.system('cmd /c "source activate"')
                        elif platform == "win32":#Windows
                            os.system('cmd /c "activate.bat"')
                        #--------------------------------------------------
                        os.system('cmd /c "pip install django"')
                        os.system('cmd /c "pip install Pillow"')
                        os.chdir("../../")
                    elif want_env == "N":
                        os.system('cmd /c "pip install django"')
                        os.system('cmd /c "pip install Pillow"')
                    else:
                        print("Worng Command",end="\n")
                else:
                    os.system('cmd /c "django-admin startapp ' + apps_name[0].capitalize())
        elif cmd_delete == "n":
            print("Project not deleted!")
            pass
        else:
            print("Wrong command!")
            pass
    else:
        os.system('cmd /c "django-admin startproject ' + project_name)
        # change the directory to the project name
        os.chdir(project_name)
        # check if the apps name is in the project directory
        if os.path.isdir(apps_name[0].capitalize()):
            print("Apps name is already in the project directory")
            exit()
        else:
            # check if apps_name has more than one app
            if len(apps_name) > 1:
                for app in apps_name:
                    os.system('cmd /c "django-admin startapp ' + app.capitalize())
                    if want_env == "Y":
                        os.system('cmd /c "pip install virtualenv"')
                        os.system('cmd /c "virtualenv env"')
                        os.chdir("env")
                        os.chdir("Scripts")
                        # Check the Operating system and start the virtualenv
                        #------------Not working on Windows 10-------------
                        if platform == "linux" or platform == "linux2":#Linux
                            os.system('cmd /c "source activate"')
                        elif platform == "darwin":#MAC OS
                            os.system('cmd /c "source activate"')
                        elif platform == "win32":#Windows
                            os.system('cmd /c "activate.bat"')
                        #--------------------------------------------------
                        os.system('cmd /c "pip install django"')
                        os.system('cmd /c "pip install Pillow"')
                        os.chdir("../../")
                    elif want_env == "N":
                        os.system('cmd /c "pip install django"')
                        os.system('cmd /c "pip install Pillow"')
                    else:
                        print("Worng Command",end="\n")
            else:
                os.system('cmd /c "django-admin startapp ' + apps_name[0].capitalize())
    # change the directory to the project name
    os.chdir('../'+project_name)

    search_text = '\nINSTALLED_APPS = [\n   "django.contrib.admin",\n  "django.contrib.auth",\n  "django.contrib.contenttypes",\n  "django.contrib.sessions",\n  "django.contrib.messages",\n  "django.contrib.staticfiles",\n'
    for app in apps_name:
        search_text += '    "' + app.capitalize() + '.apps.' +  app.capitalize() +'Config",\n'
    replace_text = search_text + ']\n'

    replace_template_dirs = "TEMPLATES = [\n\t{\n\t\t'BACKEND': 'django.template.backends.django.DjangoTemplates',\n\t\t'DIRS': [os.path.join(BASE_DIR, "'"templates"'")],\n\t\t'APP_DIRS': True,\n\t\t'OPTIONS': {\n\t\t\t'context_processors': [\n\t\t\t\t'django.template.context_processors.debug',\n\t\t\t\t'django.template.context_processors.request',\n\t\t\t\t'django.contrib.auth.context_processors.auth',\n\t\t\t\t'django.contrib.messages.context_processors.messages',\n\t\t\t],\n\t\t},\n\t},\n]\n"

    print(replace_text)
    # append the apps name to INSTALLED_APPS in settings.py
    with open(project_name + '/settings.py', 'r+') as file:
        content=file.read()
        new_file = '\n\n#----------------Replace INSTALLED_APPS with the below code----------------\/\n' + replace_text +'\n\n#----------------Leave this for STATICFILES_DIRS with the below code----------------\/\n' + "\nimport os\nSTATICFILES_DIRS = [\n\tos.path.join(BASE_DIR, 'static')\n]\n" + '\n\n#----------------Replace TEMPLATES with the below code----------------\/\n' + replace_template_dirs
        file.write(new_file)
        file.truncate()

    os.chdir('../')

    for app_name in apps_name:
        with open(project_name + '/' + app_name.capitalize() + '/views.py', 'r+') as file:
            content=file.read()
            new_file = 'def index(request):\n    return render(request,"base.html")\n'
            file.write(new_file)
            file.truncate()
        with open(project_name + '/' + app_name.capitalize() + '/urls.py', 'w+') as file:
            content=file.read()
            new_file = 'from django.urls import path\nfrom . import views\n\nurlpatterns = [\n    path("", views.index, name="index"),\n]\n'
            file.write(new_file)
            file.truncate()

    # add urls of every app to the project urls.py
    searching_text = "urlpatterns = [\n\tpath('admin/', admin.site.urls),\n"
    for app_name in apps_name:
        searching_text += "\tpath('', include('" + app_name.capitalize() + ".urls')),\n"
    replacing_text = searching_text + ']\n' + 'if settings.DEBUG:\n\turlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'

    for app_name in apps_name:
        with open(project_name + '/' + project_name + '/urls.py', 'r+') as file:
            content=file.read()
            new_file = '\n' + replacing_text + '\n'
            file.seek(0)
            file.write("from django.urls import path,include\nfrom django.contrib import admin\nfrom django.conf.urls.static import static\nfrom django.conf import settings\n")
            file.write(new_file)
            file.truncate()

    os.chdir(project_name)
    # create the templates,static directory
    os.makedirs("templates")
    os.makedirs("static")

    html_files=['index.html','base.html','about.html','contact.html','login.html',
    'newuser.html','postlist.html','postdetail.html','postcreate.html',
    'postupdate.html','postdelete.html','postcomment.html','postcommentdelete.html',
    'postcommentupdate.html','postcommentcreate.html','userupdate.html','userdelete.html',
    'userpostlistview.html','categoryview.html']

    dirs =['resoures', 'vendors']
    sub_dirs = ["css","img","js"]

    for html_file in html_files:
        open("templates/"+html_file, "w")

    dirs =['resoures', 'vendors']

    for dires in dirs:
        os.makedirs("static/" + dires)

    for sub_dir in sub_dirs:
        os.makedirs("static/resoures/" + sub_dir)

    os.makedirs("static/resoures/css/" + sub_dirs[1])

    for sub_dir in sub_dirs:
        os.makedirs("static/vendors/" + sub_dir)

    with open("static/resoures/css/style.css", "w") as file:
        file.writelines('*, \n*::before,\n*::after{\n   margin: 0;\n    padding: 0;\n box-sizing: inherit;\n}\n\nhtml{\n    font-size: 62.5%;\n\tbackground-color:pink;}\nbody{\n   font-family: "Lato", sans-serif;\n  font-weight: 400;\n line-height: 1.7;\n color: red;\n  padding: 3rem;\n   box-sizing: border-box;\n\tdisplay: grid;\n\talign-content: space-evenly;\n\tjustify-content: space-evenly;\n\talign-items: stretch;\n\tjustify-items: stretch;}\nh1{\n    font-size: 3.5rem;\n    font-weight: 900;    color: black;\n   margin: 0 auto;\n}\n')

    with open("templates/base.html", "w") as file:
        file.writelines('{% load static %}\n<html>\n\t<head>\n\t\t<title>Made with python</title>\n\t\t<link rel="stylesheet" href="{% static '"'resoures/css/style.css'"'%}">\n\t</head>\n\t<body>\n\t\t<h1>Hello World</h1>\n<h3>Do not close the terminal that is running development server(python manage.py runserver)</h3>\n\t</body>\n</html>')

    print("Django project created successfully\n------------------------------------------------\nDo not close the terminal that is running development server(python manage.py runserver)\n------------------------------------------------\n")
    os.popen('Start cmd /k "python manage.py migrate"')
    time.sleep(5)
    os.popen('Start cmd /k "python manage.py runserver"')
    time.sleep(5)
    webbrowser.open_new_tab("http://127.0.0.1:8000/")

    while True:
        for app_name in apps_name:
            # os.chdir('../')
            os.chdir('../'+project_name)
            # if KeyboardInterrupt:
            #     break
            # else:
            # Capturing the two instances models.py after certain interval of time
            # time.sleep(5)
            print("Looking for changes in " + app_name.capitalize() + " models.py\nPress 'CTRL + C' to stop the program")
            print("\nIf anything goes wrong, restart the development server\n")
            with open(app_name.capitalize() + '/models.py', 'r+') as app_models_file:
                app_models_content = app_models_file.read()
            time.sleep(5)
            with open(app_name.capitalize() + '/models.py', 'r+') as app_models_file_1:
                app_models_content_1 = app_models_file_1.read()
            # Comparing models.py after certain interval of time
            if app_models_content == app_models_content_1:
                pass
            else:
                print("\nYou made a change in " + app_name.capitalize() + " models.py file.\n")
                cmd = str(input("Did you want want to run the migration command?(y/n):"))
                if cmd == 'y':
                    os.popen('Start cmd /k python manage.py makemigrations')
                    time.sleep(4)
                    os.popen('Start cmd /k "python manage.py migrate"')
                    time.sleep(4)
                    print("\nIf you add a new model Please register your models by adding the following line to your admin.py file:\n\nfrom django.contrib import admin\nfrom . import (Model Name)\nadmin.site.register(Model Name)\n")
                elif cmd == 'n':
                    pass
                else:
                    print("Invalid input")
elif choice == 2:
    project_name = str(input("Whats your project name : ")).capitalize()
    apps_name = str(input("What your apps name : ")).split(",")
    os.chdir(project_name)
    startingPort = input("Enter the port number: ")
    if startingPort == None:
        print("You did not enter a port number")
        input("Please enter a port number")
    else:
        print(f"Starting Server on {startingPort} Port...")
        os.popen(f'Start cmd /k "python manage.py runserver 127.0.0.1:{startingPort}"')
        time.sleep(5)
        webbrowser.open_new_tab(f"http://127.0.0.1:{startingPort}/")
    while True:
        for app_name in apps_name:
            # os.chdir('../')
            # if KeyboardInterrupt:
            #     break
            # else:
            # Capturing the two instances models.py after certain interval of time
            print("Looking for changes in " + app_name.capitalize() + " models.py\nPress 'CTRL + C' to stop the program")
            print("\nIf anything goes wrong, restart the development server\n")
            with open(app_name.capitalize() + '/models.py', 'r+') as app_models_file:
                app_models_content = app_models_file.read()
            time.sleep(5)
            with open(app_name.capitalize() + '/models.py', 'r+') as app_models_file_1:
                app_models_content_1 = app_models_file_1.read()
            # Comparing models.py after certain interval of time
            if app_models_content == app_models_content_1:
                pass
            else:
                print("\nYou made a change in " + app_name.capitalize() + " models.py file.\n")
                cmd = str(input("Did you want want to run the migration command?(y/n):"))
                if cmd == 'y':
                    os.popen('Start cmd /k python manage.py makemigrations')
                    time.sleep(4)
                    os.popen('Start cmd /k "python manage.py migrate"')
                    time.sleep(4)
                    print("\nIf you add a new model Please register your models by adding the following line to your admin.py file:\n\nfrom django.contrib import admin\nfrom . import (Model Name)\nadmin.site.register(Model Name)\n")
                elif cmd == 'n':
                    pass
                else:
                    print("Invalid input")