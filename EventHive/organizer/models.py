from django.db import models

class Organizer(models.Model):
    organizer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=150)

    def __str__(self):
        return self.name
