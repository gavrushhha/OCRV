from django.contrib import admin
from ticketinfo.app.models import (
    Routes,
    Trains,
    Goods_and_services,
    Passengers,
    Purch_tickets,
    Purch_goods_services,
)

# Register your models here.


@admin.register(Routes)
class RoutesAdmin(admin.ModelAdmin):
    pass


@admin.register(Trains)
class TrainsAdmin(admin.ModelAdmin):
    pass


@admin.register(Goods_and_services)
class Goods_and_servicesAdmin(admin.ModelAdmin):
    pass


@admin.register(Passengers)
class PassengersAdmin(admin.ModelAdmin):
    pass


@admin.register(Purch_tickets)
class Purch_ticketsAdmin(admin.ModelAdmin):
    pass


@admin.register(Purch_goods_services)
class Purch_goods_servicesAdmin(admin.ModelAdmin):
    pass
