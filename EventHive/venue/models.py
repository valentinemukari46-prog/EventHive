from django.db import models
from django.db import models

class Venue(models.Model):
<<<<<<< HEAD
    venue_id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
=======
    id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
>>>>>>> af426af2917b9fe837520142fa0524121b328b9e
    capacity = models.IntegerField()

    def __str__(self):
        return self.venue_name
