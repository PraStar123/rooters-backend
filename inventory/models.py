from django.db import models
#from django.contrib.postgres.fields import ArrayField
import uuid
#from user_roles.models import operator,cleaner,attendant,driver,address


# Create your models here.
class BusSeatLayoutModel(models.Model):
    seat_layout_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number_of_seats = models.IntegerField()
    number_of_rows = models.IntegerField()
    number_of_cols = models.IntegerField()
    def __str__(self): 
         return "Number: "+str(self.number_of_seats)+" ( "+str(self.number_of_rows)+" * "+str(self.number_of_cols)+" )"
         
    


class BusConfigModel(models.Model):
    from .CONSTANTS import BUS_CLIMATE_TYPE, BUS_LAYER_TYPE, BUS_MAKE_TYPE, BUS_SEAT_STRUCTURE_TYPE, BUS_SEAT_TYPE
    bus_config_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bus_make_type = models.CharField(max_length=4, choices=BUS_MAKE_TYPE.choices, default=None)
    bus_layer_type = models.CharField(max_length=3, choices=BUS_LAYER_TYPE.choices, default=None)
    bus_seat_structure_type = models.CharField(max_length=3, choices=BUS_SEAT_STRUCTURE_TYPE.choices, default=None)
    bus_seat_type = models.CharField(max_length=30, choices=BUS_SEAT_TYPE.choices, default=None)
    #bus_seat_layout = models.ForeignKey(BusSeatLayoutModel, on_delete=models.PROTECT)
    bus_climate_type = models.CharField(max_length=3, choices=BUS_CLIMATE_TYPE.choices, default=None)
    def __str__(self): 
         return str(self.bus_make_type)+" "+str(self.bus_seat_type)+" "+str(self.bus_climate_type)+" "+str(self.bus_seat_structure_type)
         

class BusModel(models.Model):
    from .CONSTANTS import BUS_PERMIT_TYPE
    bus_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bus_name = models.CharField(max_length=50)
    bus_plate_number = models.CharField(max_length=11)
    #bus_operator = models.ForeignKey(operator, on_delete=models.CASCADE)
    bus_registration_date = models.DateField()
    bus_registered_city_area = models.CharField(max_length=50)
    bus_config = models.ForeignKey(BusConfigModel, on_delete=models.PROTECT)
    bus_permit_type = models.CharField(max_length=3, choices=BUS_PERMIT_TYPE.choices, default=None)
    #bus_permit_states = ArrayField(models.CharField(max_length=30, blank=True),blank=True,)
    def __str__(self): 
         return self.bus_name

'''
class BusDocumentModel(models.Model):
    bus_document_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bus = models.ForeignKey(BusModel, on_delete=models.CASCADE)
    #bus_pictures = ArrayField(models.BinaryField)
    #bus_documents = ArrayField(models.BinaryField)
'''

class CityModel(models.Model):
    city_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city_name = models.CharField(max_length=50)
    city_state = models.CharField(max_length=50)
    def __str__(self): 
         return self.city_name


class CityAreaModel(models.Model):
    city_area_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city_area_name = models.CharField(max_length=50)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    def __str__(self): 
         return self.city_area_name
    #landmark = models.ForeignKey(address, on_delete=models.PROTECT)


class RouteModel(models.Model):
    route_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source_city = models.ForeignKey(CityModel,related_name="source_city", on_delete=models.CASCADE)
    destination_city = models.ForeignKey(CityModel, related_name="destination_city",on_delete=models.CASCADE)
    route_distance = models.IntegerField()
    def __str__(self): 
         return str(self.source_city)+" to "+str(self.destination_city)


class SeatDetailsModel(models.Model):
    seat_details_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seat_number = models.CharField(max_length=3, blank=False)
    seat_fare = models.FloatField()
    seat_layout = models.ForeignKey(BusSeatLayoutModel, on_delete=models.CASCADE)
    is_for_ladies = models.BooleanField()


class RouteScheduleModel(models.Model):
    route_schedule_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    route_group = models.UUIDField()
    route = models.ForeignKey(RouteModel, on_delete=models.PROTECT)
    bus_config = models.ForeignKey(BusConfigModel, on_delete=models.PROTECT)
    from_date = models.DateField()
    to_date = models.DateField()
    dep_time = models.TimeField()
    arr_time = models.TimeField()
    order = models.IntegerField()
    def __str__(self): 
         return str(self.route)+"   From:  "+str(self.from_date)+ " " +str(self.dep_time)+ "  Arr:  "+str(self.to_date)+" "+str(self.arr_time)



class TripModel(models.Model):
    trip_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    route_schedule = models.ForeignKey(RouteScheduleModel, on_delete=models.CASCADE)
    trip_bus = models.ForeignKey(BusModel, on_delete=models.PROTECT)
    #trip_driver = models.ForeignKey(driver, on_delete=models.PROTECT)
    #trip_operator = models.ForeignKey(operator, on_delete=models.PROTECT)
    #trip_attendant = models.ForeignKey(attendant, on_delete=models.PROTECT)
    dep_date = models.DateField()
    arr_date = models.DateField()
    dep_time = models.TimeField()
    arr_time = models.TimeField()
    available_seats = models.IntegerField()

'''
class RestStopModel(address):
    rest_stop_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #ammenities = ArrayField(models.CharField(max_length=30, blank=True),blank=True,)
    #address = models.ForeignKey(address, on_delete=models.PROTECT)
    halt_duration = models.CharField(max_length=30)
    #rest_stop_pictures = ArrayField(models.BinaryField)
    #menu = ArrayField(models.BinaryField)
'''

class SeatModel(models.Model):
    from .CONSTANTS import SEAT_BOOKING_STATUS, SPECIAL_TYPE, WINDOW_TYPE
    seat_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    trip = models.ForeignKey(TripModel, on_delete=models.CASCADE)
    special = models.CharField(max_length=3, choices=SPECIAL_TYPE.choices, blank=False)
    seat_booking_status = models.CharField(max_length=3, choices=SEAT_BOOKING_STATUS.choices, blank=False)
    seat_detail = models.ForeignKey(SeatDetailsModel, on_delete=models.PROTECT)
    window_type = models.CharField(max_length=3, choices=WINDOW_TYPE.choices, blank=False)


class SearchModel(models.Model):
    search_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    search_group_id = models.UUIDField()
    route_group = models.CharField(max_length=50)
    from_source = models.CharField(max_length=50)
    to_dest = models.CharField(max_length=50)
    bus_config = models.CharField(max_length=50)
    dep_date = models.DateField()
    arr_date = models.DateField()
    dep_time = models.TimeField()
    arr_time = models.TimeField()
    from_order = models.IntegerField()
    to_order = models.IntegerField()