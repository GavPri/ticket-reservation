from django.db import models

class Gig(models.Models):
    name = models.CharField(max_length=100)
    venue_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.
    