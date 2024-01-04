from django.shortcuts import get_object_or_404, render

from .models import Floor

def index(request):
    #floor = get_object_or_404(Floor, floor_id)
    #floor = get_object_or_404(Floor, pk = floor_id)
    data = Floor.objects.all()
    context = { 'data' : data }
    return render(request, 'locations/display.html', context)