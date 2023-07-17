from django.shortcuts import render

# Create your views here.
def get_gig_list(request):
    return render( request, 'gig_list/giglist.html')