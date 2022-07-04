from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Routes, Goods_and_services, Passengers
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()


def findRoutes(request):
    all_routes = Routes.objects.all()

    departure = [i.start for i in all_routes]

    departure = sorted(list(set(departure)))

    data = {
        'departure': departure,
    }
    
    return render(request,
                  './Routes.html',
                  data)

def viewRoutes(request):
    start = request.POST.get('start') 

    routes = Routes.objects.filter(start=start)
    
    return render(request,
                  './viewRoutes.html',
                  {"routes": routes})


def findGoods(request):
    return render(request, './goods.html')


def viewGoods(request):
    filter_age_0_5 = request.POST.get('age_0_5')
    filter_age_6_10 = request.POST.get('age_6_10')
    filter_age_11_17 = request.POST.get('age_11_17')
    filter_age_18_55 = request.POST.get('age_18_55')
    filter_age_56_90 = request.POST.get('age_56_90')

    filter_type_service = request.POST.get('type_service')
    filter_hygiene = request.POST.get('hygiene') 
    filter_road_equipment = request.POST.get('road_equipment') 
    filter_relax = request.POST.get('relax') 
    filter_food = request.POST.get('food') 
    filter_couple = request.POST.get('couple') 
    filter_plaz = request.POST.get('plaz')

    filter_dict = {}

    if filter_age_0_5 is not None:
        filter_dict['age_0_5'] = 1
    if filter_age_6_10 is not None:
        filter_dict['age_6_10'] = 1
    if filter_age_11_17 is not None:
        filter_dict['age_11_17'] = 1
    if filter_age_18_55 is not None:
        filter_dict['age_18_55'] = 1
    if filter_age_56_90 is not None:
        filter_dict['age_56_90'] = 1
    
    if filter_type_service is not None:
        filter_dict['type_service'] = 1
    if filter_hygiene is not None:
        filter_dict['kind_hygiene'] = 1
    if filter_road_equipment is not None:
        filter_dict['kind_road_equipment'] = 1

    if filter_relax is not None:
        filter_dict['kind_relax'] = 1
    if filter_food is not None:
        filter_dict['kind_food'] = 1
    if filter_couple is not None:
        filter_dict['available_coupe'] = 1
    if filter_plaz is not None:
        filter_dict['available_plaz'] = 1

    find_goods = Goods_and_services.objects.filter(**filter_dict)

    data = {
        'find_goods': find_goods,
    }
    
    return render(request, './viewGoods.html', data)


def loginform(request):
    return render(request, './login.html')


def login(request):
    u = request.POST
    user = authenticate(request, username=u['username'], password=u['password'])
    if user is not None:
        auth_login(request, user)
        context = {
            'msg': "Login Successsful"
        }
    else:
        context = {
            'msg': "Error User is not registered/invalid"
        }

    return render(request, './error.html', context)


def registerform(request):
    return render(request, './register.html')


def render_profile(request):
    return render(request, './profile.html')


def profile(request):
        username = request.POST['username']
        pas_id = User.objects.get(username=username).id
        age = request.POST['age']
        sex = request.POST['sex']
        marit_status = request.POST['marit_status']
        education = request.POST['education']
        childs = request.POST['childs']

        passenger = Passengers.objects.filter(id=pas_id).update(age=age, sex=sex, marit_status=marit_status, education=education, childs=childs)

        context = {
            'msg': "Successsful"
        }

        return render(request, './error.html', context)


def my_profile(request):
    try:
        person = User.objects.get(username=request.user.username).id
        info = Passengers.objects.filter(id=person)
        return render(request, './my_profile.html', {'info': info})
    except:
        return render(request, './error.html', {'msg': "Error"})



def register(request):
    count_id = Passengers.objects.all().count()
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    
    user = User.objects.create_user(id=count_id+1, username=username, email=email, first_name=first_name, last_name=last_name, password=password)
    passenger = Passengers.objects.create(id=count_id+1)
    user.save()
    passenger.save()

    context = {
        'msg': "Registeration Successsful"
    }

    return render(request, './error.html', context)


def logout(request):
    auth_logout(request)

    context = {
        'msg': "Logout Successful"
    }

    return render(request, './error.html', context)


def mybooking(request):
    try:
        if request.user.is_authenticated:
            person = User.objects.get(username=request.user.username).id
            info = Passengers.objects.filter(id=person)
            return render(request, './mybooking.html', {'ticket': ticket})
        else:
            return render(request, './error.html', {'msg': "User not authenticated"})
    except:
        return render(request, './error.html', {'msg': "Error"})


def render_book(request, id):
    context = {
        'msg': "This function is disabled"
    }
    return render(request, './error.html', context)


def render_book_goods(request):
    context = {
        'msg': "This function is disabled"
    }
    return render(request, './error.html', context)

