# EmployeeManager

I created this code on Ubuntu 20.04 so all the commands I will list to run the application will be for linux.

I attempted to create a docker image for this project but the requirements would not install on the docker image and I could not resolve the issue.

I recommend using a ubuntu virtual machine to run this code. I will provide a deploy.sh script to run all these commands. I have tested running these commands on a Ubuntu VM so I know they work.

If you want to run from windows this link will provide the code: 
https://www.geeksforgeeks.org/clone-and-run-a-django-project-from-github/

However, when I attempted to run this on a windows machine, I could not run the script to activate the virtual environment which Django needs to run because running scripts is not enabled by default like it is on Ubuntu.

##Commands:

###Install Packages
```
sudo apt install git
sudo apt install python3
sudo apt install pip
sudo apt install python3.8-venv
```

###Enable Virtual Enviroment
```
python3 -m venv venv
source venv/bin/activate 
```

###Clone Repository
```
git clone --branch secure https://github.com/adamregan53/EmployeeManager.git
```
OR

```
git clone --branch insecure https://github.com/adamregan53/EmployeeManager.git
```

###Move venv into project directory
```
mv venv EmployeeManager
cd EmployeeManager
```

###Install project requirements
```
pip install -r requirements.txt
pip install crispy-bootstrap5
```

###Run Server
```
python manage.py runserver
```
