"""Models for the vendorEventRegister app."""

from django.db import models


class Events(models.Model):
    """Model representing an event."""
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_description = models.TextField()
    registration_close_date = models.DateField()
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.event_name