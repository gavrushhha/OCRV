from django.db import models
from django.utils.translation import gettext_lazy as _

# from matplotlib.style import available

# Create your models here.
class Id(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        abstract = True


class Routes(Id):
    start = models.CharField(_("start"), max_length=255)
    route_time = models.IntegerField(_("route_time"), blank=True)
    end = models.CharField(_("end"), max_length=255)

    def __str__(self):
        return self.start + " - " + self.end

    class Meta:
        # constraints = [models.UniqueConstraint(fields=["name"], name="unique_train")]
        db_table = "routes"
        verbose_name = _("routes")
        verbose_name_plural = _("routes")


class Trains(Id):
    num_trains = models.CharField(_("num_trains"), max_length=255)
    time_departure = models.IntegerField(_("time_departure"), blank=True)
    time_arrival = models.IntegerField(_("time_arrival"), blank=True)
    plaz_count = models.IntegerField(_("plaz_count"), blank=True)
    coupe_count = models.IntegerField(_("coupe_count"), blank=True)
    sv_count = models.IntegerField(_("sv_count"), blank=True)
    route = models.ForeignKey(
        Routes,
        verbose_name=_("routes"),
        on_delete=models.CASCADE,
        related_name="routes",
    )

    def __str__(self):
        return self.num_trains

    class Meta:
        # constraints = [models.UniqueConstraint(fields=["name"], name="unique_train")]
        db_table = "trains"
        verbose_name = _("trains")
        verbose_name_plural = _("trains")


class Goods_and_services(Id):
    name = models.CharField(_("name"), max_length=255)
    price = models.IntegerField(_("price"), blank=True)
    age_0_5 = models.BooleanField(_("age_0_5"), blank=True)
    age_6_10 = models.BooleanField(_("age_6_10"), blank=True)
    age_11_17 = models.BooleanField(_("age_11_17"), blank=True)
    age_18_55 = models.BooleanField(_("age_18_55"), blank=True)
    age_56_90 = models.BooleanField(_("age_56_90"), blank=True)
    type_service = models.BooleanField(_("type_service"), blank=True)
    kind_hygiene = models.BooleanField(_("kind_hygiene"), blank=True)
    kind_road_equipment = models.BooleanField(_("kind_road_equipment"), blank=True)
    kind_relax = models.BooleanField(_("kind_relax"), blank=True)
    kind_food = models.BooleanField(_("kind_food"), blank=True)
    available_coupe = models.BooleanField(_("available_coupe"), blank=True)
    available_plaz = models.BooleanField(_("available_plaz"), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        # constraints = [models.UniqueConstraint(fields=["name"], name="unique_train")]
        db_table = "goods_and_services"
        verbose_name = _("goods_and_services")
        verbose_name_plural = _("goods_and_services")


class Passengers(Id):
    sex = models.CharField(_("sex"), max_length=255)
    age = models.IntegerField(_("age"), blank=True)
    marit_status = models.CharField(_("marit_status"), max_length=255)
    education = models.CharField(_("education"), max_length=255)
    childs = models.IntegerField(_("childs"), blank=True)
    networks_fb = models.BooleanField(_("networks_fb"), blank=True)
    networks_inst = models.BooleanField(_("networks_inst"), blank=True)
    networks_tt = models.BooleanField(_("networks_tt"), blank=True)
    networks_vk = models.BooleanField(_("networks_vk"), blank=True)
    networks_ok = models.BooleanField(_("networks_ok"), blank=True)

    def __str__(self):
        return self.sex

    class Meta:
        # constraints = [models.UniqueConstraint(fields=["name"], name="unique_train")]
        db_table = "passengers"
        verbose_name = _("passengers")
        verbose_name_plural = _("passengers")


class Purch_tickets(Id):
    type_wagon = models.CharField(_("sex"), max_length=255)
    num_wagon = models.IntegerField(_("num_wagon"), blank=True)
    num_seat = models.IntegerField(_("num_seat"), blank=True)
    train = models.ForeignKey(
        Trains, verbose_name=_("train"), on_delete=models.CASCADE, related_name="train"
    )
    passengers = models.ForeignKey(
        Passengers,
        verbose_name=_("passengers"),
        on_delete=models.CASCADE,
        related_name="passengers",
    )

    price = models.FloatField(_("price"), blank=True)
    dates_purchase = models.DateTimeField()

    def __str__(self):
        return self.type_wagon

    class Meta:
        # constraints = [models.UniqueConstraint(fields=["name"], name="unique_train")]
        db_table = "purch_tickets"
        verbose_name = _("purch_tickets")
        verbose_name_plural = _("purch_tickets")


class Purch_goods_services(Id):
    ticket = models.ForeignKey(
        Purch_tickets,
        verbose_name=_("ticket"),
        on_delete=models.CASCADE,
        related_name="ticket",
    )
    gs = models.ForeignKey(
        Goods_and_services,
        verbose_name=_("gs"),
        on_delete=models.CASCADE,
        related_name="gs",
    )

    # def __str__(self):
    #     return self.sex

    class Meta:
        # constraints = [models.UniqueConstraint(fields=["name"], name="unique_train")]
        db_table = "purch_goods_services"
        verbose_name = _("purch_goods_services")
        verbose_name_plural = _("purch_goods_services")
