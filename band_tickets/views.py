from django.shortcuts import render
from .models import Gig

# Create your views here.


def get_gig_list(request):
    gigs = Gig.objects.all()
    context = {
        'gigs': gigs
    }
    return render(request, 'gig_list/giglist.html', context)
