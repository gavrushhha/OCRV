import typing as tp
from pytest import fixture


@fixture
def init_route() -> tp.Dict[str, tp.Any]:
    return {"start": "Start", "route_time": 13, "end": "End"}


@fixture
def init_train() -> tp.Dict[str, tp.Any]:
    init_kwargs = {
        "num_trains": "1234",
        "time_departure": 13,
        "time_arrival": 1234,
        "plaz_count": 1,
        "coupe_count": 1,
        "sv_count": 1,
        "route": None,
    }

    return init_kwargs


@fixture
def init_passenger() -> tp.Dict[str, tp.Any]:
    init_kwargs = {
        "sex": "Ж",
        "age": 123,
        "childs": 12,
        "networks_fb": 1,
        "networks_inst": 1,
        "networks_tt": 1,
        "networks_vk": 1,
        "networks_ok": 1,
    }

    return init_kwargs


@fixture
def init_gas() -> tp.Dict[str, tp.Any]:
    init_kwargs = {
        "name": "name",
        "price": 123,
        "age_0_5": 1,
        "age_6_10": 0,
        "age_11_17": 0,
        "age_18_55": 0,
        "age_56_90": 1,
        "type_service": 1,
        "kind_hygiene": 1,
        "kind_road_equipment": 1,
        "kind_relax": 1,
        "kind_food": 1,
        "available_coupe": 1,
        "available_plaz": 1,
    }

    return init_kwargs


@fixture
def init_ticket() -> tp.Dict[str, tp.Any]:
    init_kwargs = {
        "type_wagon": "type",
        "num_wagon": 123,
        "num_seat": 123,
        "train": None,
        "passengers": None,
        "price": 123,
        "dates_purchase": "2021-07-24 00:00:00.000",
    }

    return init_kwargs
