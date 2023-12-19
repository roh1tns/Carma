from django.shortcuts import render

# Create your views here.
def far(request):
    return render(request, "far/find_a_ride.html")