sed -i 's/DEBUG = True/DEBUG = False/' config/settings/env.py   # Set debug to off
python3 manage.py makemigrations
python3 manage.py migrate
