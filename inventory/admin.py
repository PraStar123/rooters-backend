from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BusConfigModel)
admin.site.register(BusModel)
admin.site.register(BusSeatLayoutModel)
admin.site.register(SeatDetailsModel)
admin.site.register(SeatModel)
admin.site.register(TripModel)
admin.site.register(CityAreaModel)
admin.site.register(CityModel)
admin.site.register(RouteScheduleModel)
admin.site.register(RouteModel)
admin.site.register(SearchModel)
