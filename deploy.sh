sudo apt install git
sudo apt install python3
sudo apt install pip
sudo python3 -m pip install Django
sudo apt install python3.8-venv
python3 -m venv venv
source venv/bin/activate
git clone --branch secure https://github.com/adamregan53/EmployeeManager.git
mv venv EmployeeManager
cd EmployeeManager
pip install -r requirements.txt
pip install crispy-bootstrap5
python manage.py runserver

