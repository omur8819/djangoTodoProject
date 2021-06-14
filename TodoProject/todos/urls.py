from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_todo_items, name="todo_list"),
    path('insert_todo/',views.insert_todo_item, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item, name='delete_todo_item'),
    path('edit_todo/<int:todo_id>/',views.edit_todo_item, name='edit_todo_item'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path("update/<int:todo_id>/", views.todo_update, name="todo-update")
]