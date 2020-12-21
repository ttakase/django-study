from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()

    # オブジェクトのリターンを表示して管理画面で見やすいように表示する
    def __str__(self):
        return self.title