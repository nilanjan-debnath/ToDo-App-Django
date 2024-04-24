from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=350)
    details=models.CharField(max_length=1000, default=None)
    complete=models.BooleanField(default=False)
    addtime=models.DateField(default=timezone.now)
    finishtime=models.DateField(default=None)

    def __str__(self):
        return self.title