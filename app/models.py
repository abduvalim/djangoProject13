
from django.db import models


class User(models.Model):
    fullname = models.CharField(max_length=155)
    image = models.ImageField(upload_to='user/')
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return self.fullname



