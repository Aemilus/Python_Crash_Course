### How to run Learning Log project on Windows

1. Open PowerShell in project dir
2. Change PowerShell prompt to a short string.
```
Function prompt {"CMD "}
```
3. Activate venv. You might need to recreate venv.
```
.\ll_env\Scripts\activate
```
4. Start Django server
```
python manage.py runserver
```
5. Browse to http://localhost:8000

### Accounts
```
ll_admin / admin
testuser / django..
testuser2 / django2..
```
