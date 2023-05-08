from django.db import models

# Create your models here.
class task(models.Model):
    list=models.CharField(max_length=100)
    complete=models.BooleanField(default=False)
    time=models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.list
