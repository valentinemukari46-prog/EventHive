from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name
