from django.core.handlers.wsgi import WSGIRequest
from django.utils.datastructures import MultiValueDictKeyError
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from ticketinfo.app.models import (
    Routes,
    Goods_and_services,
    Passengers,
    Purch_tickets,
    Purch_goods_services,
)
from dotenv import load_dotenv

load_dotenv()


def findRoutes(request: WSGIRequest) -> HttpResponse:
    """
    Функция берет все города отправления из Routes, делает из него set.
    """
    all_routes = Routes.objects.all()
    departure = [i.start for i in all_routes]
    departure = sorted(list(set(departure)))
    data = {
        "departure": departure,
    }

    return render(request, "./Routes.html", data)


def viewRoutes(request: WSGIRequest) -> HttpResponse:
    """
    Функция отображает запрос на поиск поездок по определенному городу.
    """
    start = request.POST.get("start")
    routes = Routes.objects.filter(start=start)

    if start is not None:
        return render(request, "./viewRoutes.html", {"routes": routes})
    else:
        context = {"msg": "You haven't entered anything"}
        return render(request, "./error.html", context)


def viewGoods(request: WSGIRequest) -> HttpResponse:
    """
    Функция делает фильтрацию товаров.
    """
    filter_age_0_5 = request.POST.get("age_0_5")
    filter_age_6_10 = request.POST.get("age_6_10")
    filter_age_11_17 = request.POST.get("age_11_17")
    filter_age_18_55 = request.POST.get("age_18_55")
    filter_age_56_90 = request.POST.get("age_56_90")

    filter_type_service = request.POST.get("type_service")
    filter_hygiene = request.POST.get("hygiene")
    filter_road_equipment = request.POST.get("road_equipment")
    filter_relax = request.POST.get("relax")
    filter_food = request.POST.get("food")
    filter_couple = request.POST.get("couple")
    filter_plaz = request.POST.get("plaz")

    filter_dict = {}

    if filter_age_0_5 is not None:
        filter_dict["age_0_5"] = 1
    if filter_age_6_10 is not None:
        filter_dict["age_6_10"] = 1
    if filter_age_11_17 is not None:
        filter_dict["age_11_17"] = 1
    if filter_age_18_55 is not None:
        filter_dict["age_18_55"] = 1
    if filter_age_56_90 is not None:
        filter_dict["age_56_90"] = 1

    if filter_type_service is not None:
        filter_dict["type_service"] = 1
    if filter_hygiene is not None:
        filter_dict["kind_hygiene"] = 1
    if filter_road_equipment is not None:
        filter_dict["kind_road_equipment"] = 1

    if filter_relax is not None:
        filter_dict["kind_relax"] = 1
    if filter_food is not None:
        filter_dict["kind_food"] = 1
    if filter_couple is not None:
        filter_dict["available_coupe"] = 1
    if filter_plaz is not None:
        filter_dict["available_plaz"] = 1

    find_goods = Goods_and_services.objects.filter(**filter_dict)

    data = {
        "find_goods": find_goods,
    }

    return render(request, "./viewGoods.html", data)


def findGoods(request: WSGIRequest) -> HttpResponse:
    """
    Функция отображает запрос по поиску товаров на ./goods.html.
    """
    return render(request, "./goods.html")


def login(request: WSGIRequest) -> HttpResponse:
    """
    Функция авторизации пользователя.
    """
    try:
        u = request.POST
        user = authenticate(request, username=u["username"], password=u["password"])
        if user is not None:
            auth_login(request, user)
            context = {"msg": "Login Successsful"}
        else:
            context = {"msg": "Error User is not registered/invalid"}

    except MultiValueDictKeyError:
        context = {"msg": "Error"}
    return render(request, "./error.html", context)


def loginform(request: WSGIRequest) -> HttpResponse:
    """
    Функция отображает запрос на ./login.html.
    """
    return render(request, "./login.html")


def register(request: WSGIRequest) -> HttpResponse:
    """
    Функция регистрации пользователя.
    """
    try:
        count_id = Passengers.objects.all().count()
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        user = User.objects.create_user(
            id=count_id + 1,
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        passenger = Passengers.objects.create(id=count_id + 1)
        user.save()
        passenger.save()

        context = {"msg": "Registeration Successsful"}

    except MultiValueDictKeyError:
        context = {"msg": "Error"}
    except IntegrityError:
        context = {"msg": "Please enter a different name"}

    return render(request, "./error.html", context)


def registerform(request: WSGIRequest) -> HttpResponse:
    """
    Функция отображает запрос на ./register.html.
    """
    return render(request, "./register.html")


def profile(request: WSGIRequest) -> HttpResponse:
    """
    Функция добавления дополнительных данных пользователя в Passangers.
    """
    try:
        pas_id = User.objects.get(username=request.user.username).id
        age = request.POST["age"]
        sex = request.POST["sex"]
        marit_status = request.POST["marit_status"]
        education = request.POST["education"]
        childs = request.POST["childs"]

        Passengers.objects.filter(id=pas_id).update(
            age=age,
            sex=sex,
            marit_status=marit_status,
            education=education,
            childs=childs,
        )

        context = {"msg": "Successsful"}

    except ObjectDoesNotExist:
        context = {"msg": "Error User is not registered/invalid"}

    return render(request, "./error.html", context)


def render_profile(request: WSGIRequest) -> HttpResponse:
    """
    Функция рендерит ./profile.html.
    """
    if request.user.is_authenticated:
        return render(request, "./profile.html")
    else:
        context = {"msg": "Error User is not registered/invalid"}
        return render(request, "./error.html", context)


def my_profile(request: WSGIRequest) -> HttpResponse:
    """
    Функция отображает дополнительные данные пользователя на ./profile.html.
    """
    try:
        person = User.objects.get(username=request.user.username).id
        info = Passengers.objects.filter(id=person)
        return render(request, "./my_profile.html", {"info": info})

    except ObjectDoesNotExist:
        context = {"msg": "Error User is not registered/invalid"}
        return render(request, "./error.html", context)


def logout(request: WSGIRequest) -> HttpResponse:
    """
    Функция выхода пользователя с сайта.
    """
    auth_logout(request)

    context = {"msg": "Logout Successful"}

    return render(request, "./error.html", context)


def mybooking(request: WSGIRequest) -> HttpResponse:
    """
    Функция, которая показывает историю покупок пользователя.
    """
    try:
        person = User.objects.get(username=request.user.username).id
        tickets = Purch_tickets.objects.filter(passengers=person)
        if tickets.count() == 0:
            context = {"msg": "No items"}
            return render(request, "./error.html", context)

        return render(request, "./mybooking.html", {"tickets": tickets})

    except ObjectDoesNotExist:
        context = {"msg": "Error User is not registered/invalid"}
        return render(request, "./error.html", context)


def render_book(request: WSGIRequest, id: int) -> HttpResponse:
    """
    Функция для отображения при нажатии кнопки "купить".
    """
    if request.user.is_authenticated:
        context = {"msg": "This function is disabled"}
    else:
        context = {"msg": "Error User is not registered/invalid"}

    return render(request, "./error.html", context)


def mybooking_goods(request: WSGIRequest, ticket_id: int) -> HttpResponse:
    """
    По результатам можно итерироваться.
    Доступные колонки - ['id', 'name', 'gs_id', 'price', 'cnt']
    из которых нужны только name, price, cnt (число)
    """
    if request.user.is_authenticated:
        stmt = (
            "SELECT id, name, gs_id, price, COUNT(gs_id) AS cnt\n"
            "FROM (\n"
            "    SELECT purch_goods_services.id, name, gs_id, price FROM purch_goods_services\n"  # noqa: E501
            "    JOIN recsys.goods_and_services\n"
            "    ON goods_and_services.id = purch_goods_services.gs_id\n"
            f"    WHERE recsys.purch_goods_services.ticket_id = {ticket_id}\n"
            ") AS mtbl\n"
            "GROUP BY mtbl.gs_id\n"
        )
        result = Purch_goods_services.objects.raw(stmt)

        ticket = Purch_tickets.objects.get(id=ticket_id)
        all_price = 0

        for i in result:
            all_price += i.price * i.cnt

        all_price += ticket.price

        return render(
            request,
            "./mybooking_goods.html",
            {"result": result, "all_price": all_price},
        )
    else:
        context = {"msg": "Error User is not registered/invalid"}
        return render(request, "./error.html", context)


def render_book_goods(request: WSGIRequest) -> HttpResponse:
    """
    Функция для отображения при нажатии кнопки "купить".
    """
    if request.user.is_authenticated:
        context = {"msg": "This function is disabled"}
    else:
        context = {"msg": "Error User is not registered/invalid"}

    return render(request, "./error.html", context)
