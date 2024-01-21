from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

from .models import Desk, Booking
from locations.models import Site, Floor
from website import settings

def get_floors(request, site_id):
    query = Floor.objects.filter(site_id = site_id)
    return JsonResponse({'floors': list(query.values())})
    
def get_desks(request, floor_id):
    query = Desk.objects.filter(floor_id = floor_id)
    return JsonResponse({'desks': list(query.values())})
    
def get_bookings(request, desk_id, start_datetime, end_datetime):
    query = Booking.objects.filter(
        desk_id = desk_id,
        end_time__gt = datetime.fromisoformat(start_datetime),
        start_time__lt = datetime.fromisoformat(end_datetime),
    )
    print(datetime.fromisoformat(start_datetime), " ", datetime.fromisoformat(end_datetime));
    return JsonResponse({'bookings': list(query.values())})

def get_available_desks(request):

    
    condition = request.GET.get('site')
    #Retrieve 
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')
    
    #Determine the ids of desks booked in this period:
    booked_desks = Booking.object.filter(
        
    )


def index(request):
    print(Site.objects.all().order_by('name').values())
    context = {
        'alphabetical_labels': ["a", "b"],
        'sites': Site.objects.all().order_by('name').values(),
    }
    return render(request, 'desks/index.html', context)
    