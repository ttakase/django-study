from django.shortcuts import render
from django.views.generic.list import ListView
from .models import TodoModel
# listviewの継承
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#listview
class Todolist(ListView): 
  template_name = 'list.html' # template_nameはLiistviewで定義されている
  model = TodoModel # models.py内にデータの定義がされているのでそれと関連付ける設定
