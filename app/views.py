from django.shortcuts import render
from .models import Station, Route

def stations_view(request):
    routes = Route.objects.all()

    context = {
        'routes': routes,
    }

    route = request.GET.get('route')
    if route:
        stations = routes.get(name=route).stations.all()
        context['stations'] = stations

        stations = stations.order_by('longitude')
        st_first = stations.first()
        st_last = stations.last()
        y = (st_first.longitude + st_last.longitude) / 2

        stations = stations.order_by('latitude')
        st_first = stations.first()
        st_last = stations.last()
        x = (st_first.latitude + st_last.latitude ) / 2

        context['center'] = {'x': x, 'y': y}
    else:
        context['center'] = {'x':'55.75370903771494', 'y': '37.61981338262558', }
    print(context)

    return render(request, 'stations.html', context)

