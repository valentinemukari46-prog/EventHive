from django.db import models

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=150)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    event_date = models.DateField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    available_tickets = models.IntegerField()

    def __str__(self):
        return self.event_name
