# Description
project to improve knowledge
## Technology stack
- JWT
- DRF
- PostgresSQL

## How to run

Clone the repository:

```sh
https://github.com/Artsiom-Shlapakou/task_api.git
```

Create and activate virtualenv:

```sh
virtualenv -p python3 .env
source .env/bin/activate
```
Install dependencies:
```sh
../backend  pip install -r requirements.txt
```
Run migrations:
```sh
../backend  python manage.py makemigrations
../backend  python manage.py migrate
```
Start up backend:
```sh
../backend python manage.py runserver
```
