from django.urls import path, include # call app
from .views import Todolist

urlpatterns = [
    path('list/', Todolist.as_view()),
]