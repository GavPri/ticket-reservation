from django.db import models

class Gig(models.Models):
    venue_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    