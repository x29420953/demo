from django.urls import path
from todolist import views

urlpatterns = [
    path('todolist/', views.ToDoListAllView.as_view(), name='todolist_getall'),
    path('todolist/<int:id>/', views.ToDoListView.as_view(), name="todolist_get")
]
