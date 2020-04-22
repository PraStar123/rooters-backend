from django.shortcuts import render
from django.core import serializers
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RouteModel, RouteScheduleModel, CityModel
from .Serializers import RouteScheduleSerializers, BusConfigSerializers, SearchModelSerializers
import datetime 
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import json
import uuid

class result(object):
    def __init__(self, route_group, from_source, to_dest, bus_config, dep_date, arr_date, dep_time, arr_time, from_order,to_order ):
        self.route_group = route_group 
        self.from_source = from_source 
        self.to_dest = to_dest 
        self.bus_config = bus_config
        self.dep_time = dep_time 
        self.arr_time = arr_time 
        self.dep_date = dep_date 
        self.arr_date = arr_date 
        self.from_order = from_order 
        self.to_order = to_order 


class SearchAPIView(APIView):
    def get(self, request):
        
        # Get query params
        from_source = request.GET['from']
        to_dest = request.GET['to']
        date = request.GET['date']
        on_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        print("Received query params")

        # Get the routes
        routes_from_source = get_routes_by_source(from_source)
        routes_to_dest = get_routes_by_dest(to_dest)
        print("Retrieved routes list")

        # Get buses for the described routes
        route_schedules_from_source = RouteScheduleModel.objects.filter(route__in=routes_from_source,
                                        from_date__lte=on_date, to_date__gte=on_date).select_related('bus_config')
        route_schedules_to_dest = RouteScheduleModel.objects.filter(route__in=routes_to_dest, 
                                        from_date__lte=on_date, to_date__gte=on_date).select_related('bus_config')
        print("Retrieved route shedules")
     
        available_buses = search_result(route_schedules_from_source, route_schedules_to_dest)
        print('Got available buses')

        result_list = []
        for pair in available_buses: 
            route_group = pair[0].route_group
            dep_time = pair[0].dep_time.__str__()
            arr_time = pair[1].arr_time.__str__()
            bus_config = pair[0].bus_config.__str__()
            from_order = pair[0].order.__str__()
            to_order = pair[1].order.__str__()
            data_dict = dict(
                route_group= route_group.__str__(),
                from_source=from_source,
                to_dest= to_dest,
                bus_config= bus_config,
                dep_date=on_date.__str__(),
                arr_date= on_date.__str__(),
                dep_time= dep_time,
                arr_time= arr_time,
                from_order= from_order,
                to_order= to_order
            )
        
            result_list.append(data_dict)
            
        
        return Response(json.dumps(result_list))

def get_routes_by_source(source):
    source_city_id = get_city_id(source)
    routes = RouteModel.objects.filter(source_city=source_city_id)
    print("Routes from source found " )
    return routes

def get_routes_by_dest(dest):
    dest_city_id = get_city_id(dest)
    routes = RouteModel.objects.filter(destination_city=dest_city_id)
    print("Routes to dest found")
    return routes

def get_city_id(city):
    city = CityModel.objects.get(city_name=city)
    print("Got city " + city.city_name)
    return city.city_id

def search_result(route_schedules_a, route_schedules_b):
    result = []
    #serializer = RouteScheduleSerializers.RouteScheduleDisplaySerializer() 
    for a in route_schedules_a:
        for b in route_schedules_b:
            if a.route_group == b.route_group:
                result.append([a, b])

    print(len(result))
    return result
