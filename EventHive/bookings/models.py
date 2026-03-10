from django.db import models

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tickets_booked = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateField()

    def __str__(self):
        return f"Booking {self.booking_id}"
