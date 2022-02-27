### How to run Learning Log project locally on Windows

1. Open PowerShell in project dir
```
Python_Crash_Course__by__Eric_Matthes\Project\project03\learning_log
```
2. Change PowerShell prompt to a short string.
```
Function prompt {"CMD "}
```
3. Activate project venv
```
.\ll_env\Scripts\activate
```
- if you need to recreate the venv then (also check _requirements.txt_)
```
python -m venv ll_env
.\ll_env\Scripts\activate
pip install django
pip install django-bootstrap4
```
4. Start Django server
```
python manage.py runserver
```
5. Browse to http://localhost:8000
6. When done
```
CTRL+C
deactivate
```

### Accounts
```
admin / admin..
ll_admin / admin
testuser / django..
testuser2 / django2..
```
