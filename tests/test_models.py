import pytest
import typing as tp

from django.db import models

from ticketinfo.app.models import (
    Routes,
    Trains,
    Passengers,
    Goods_and_services,
    Purch_goods_services,
    Purch_tickets,
)


def create_and_get(cls: models.Model, init_kwargs: tp.Dict[str, tp.Any]):
    cls.objects.create(**init_kwargs)
    return cls.objects.get(pk=1)


@pytest.mark.django_db
def test_routes(init_route: tp.Dict[str, tp.Any]) -> None:
    Routes.objects.create(**init_route)
    assert Routes.objects.count() == 1


@pytest.mark.django_db
def test_trains(
    init_route: tp.Dict[str, tp.Any], init_train: tp.Dict[str, tp.Any]
) -> None:
    route = create_and_get(Routes, init_route)
    init_train["route"] = route
    Trains.objects.create(**init_train)
    assert Trains.objects.count() == 1


@pytest.mark.django_db
def test_passengers(init_passenger: tp.Dict[str, tp.Any]) -> None:
    Passengers.objects.create(**init_passenger)
    assert Passengers.objects.count() == 1


@pytest.mark.django_db
def test_gas(init_gas: tp.Dict[str, tp.Any]) -> None:
    Goods_and_services.objects.create(**init_gas)
    assert Goods_and_services.objects.count() == 1


@pytest.mark.django_db
def test_purch_gs(
    init_gas: tp.Dict[str, tp.Any],
    init_ticket: tp.Dict[str, tp.Any],
    init_train: tp.Dict[str, tp.Any],
    init_route: tp.Dict[str, tp.Any],
    init_passenger: tp.Dict[str, tp.Any],
) -> None:
    route = create_and_get(Routes, init_route)
    init_train["route"] = route
    train = create_and_get(Trains, init_train)
    passeng = create_and_get(Passengers, init_passenger)
    init_ticket["train"] = train
    init_ticket["passengers"] = passeng
    ticket = create_and_get(Purch_tickets, init_ticket)
    gs = create_and_get(Goods_and_services, init_gas)
    Purch_goods_services.objects.create(ticket=ticket, gs=gs)

    assert Purch_goods_services.objects.count() == 1


@pytest.mark.django_db
def test_purch_tick(
    init_route: tp.Dict[str, tp.Any],
    init_ticket: tp.Dict[str, tp.Any],
    init_train: tp.Dict[str, tp.Any],
    init_passenger: tp.Dict[str, tp.Any],
) -> None:
    route = create_and_get(Routes, init_route)
    init_train["route"] = route
    train = create_and_get(Trains, init_train)
    passeng = create_and_get(Passengers, init_passenger)
    init_ticket["train"] = train
    init_ticket["passengers"] = passeng
    Purch_tickets.objects.create(**init_ticket)
    assert Purch_tickets.objects.count() == 1
