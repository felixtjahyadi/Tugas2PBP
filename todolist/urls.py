from django.urls import path
from todolist.views import show_todolist
from todolist.views import register 
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import change_status
from todolist.views import delete
from todolist.views import show_json
from todolist.views import add_ajax
# from todolist.views import delete_ajax
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('change-status/<int:pk>', change_status, name='change_status'),
    path('delete/<int:pk>', delete, name='delete'),
    path('json/', show_json, name='show_json'),
    path('add/', add_ajax, name='add-task'),
    # path('delete-ajax/', delete_ajax, name='delete_ajax')
]