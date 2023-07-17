from django.db import models
from django import forms

class Gig(models.Model):
    name = models.CharField(max_length=100)
    venue_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class BookingForm(models.Model):
    user_fname = forms.CharField(max_length=25, label='fname')
    user_lname = forms.CharField(max_length=25, label='lname')
    quantity = forms.IntegerField(min_value=1, max_value=3, label='Quantity', initial=1)
    user_email = forms.EmailField(label='Email')