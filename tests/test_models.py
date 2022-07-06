import pytest

from ticketinfo.app.models import Routes


@pytest.mark.django_db
def test_routes():
    init_kwargs = {"start": "Start", "route_time": 13, "end": "End"}
    Routes.objects.create(**init_kwargs)
    assert Routes.objects.count() == 1
