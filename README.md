# YATUBE_API
### Project description
This project is API for social networking website 'Yatube'.
- Python 3.9.10
- Django 3.2.14
- djangorestframework 3.12.4
- djangorestframework-simplejwt 4.7.2
### Instructions for working with this project
1) Clone this repositoy to your PC with the following command in the terminal:
``` git clone https://github.com/anastaciakaz/api_final_yatube.git ```
2) Open the directory and activate virtual environment in the terminal:
```
python -m venv venv
```
3) Activate virtual environment:
```
source venv/Scripts/activate
```
4) Update pip:
```
python -m pip install --upgrade pip
```
5) Install requirements:
```
pip install -r requirements.txt
``` 
6) Run migrations:
```
python manage.py migrate
```
7) Run server:
```
python manage.py runserver
```
### Access to the project: 
```
http://127.0.0.1:8000/api/v1/
```
### Examples of the requests to API:
- The list of all posts (GET-request):
```
http://127.0.0.1:8000/api/v1/posts/
```
- Certain post (GET-request):
```
http://127.0.0.1:8000/api/v1/posts/1/
```
- The list of all groups (GET-request):
```
http://127.0.0.1:8000/api/v1/groups/
```
- The list of all comments of a certain post (GET-request):
```
http://127.0.0.1:8000/api/v1/posts/1/comments/
```
- Create a new post (POST-request, JWT authentication is required):
```
http://127.0.0.1:8000/api/v1/posts/
```
