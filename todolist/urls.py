from django.urls import path
from todolist.views import delete_task_ajax, todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import delete
from todolist.views import show_json
from todolist.views import delete_task_ajax
from todolist.views import create_task_ajax




app_name = "todolist"

urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete/<int:id>', delete, name='delete'),
    path('json/', show_json, name='show_json'),
    path('delete/<id>', delete_task_ajax, name='delete-task-ajax'),
    path('add/', create_task_ajax, name='create-task-ajax'),
]