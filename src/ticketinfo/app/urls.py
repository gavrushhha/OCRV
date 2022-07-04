from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.findRoutes, name="findRoutes"),
    path('viewRoutes/', views.viewRoutes, name="viewRoutes"),
    path('goods/', views.findGoods, name="findGoods"),
    path('viewGoods/', views.viewGoods, name="viewGoods"),
    path('loginform/',views.loginform,name="loginform"),
    path('login/',views.login,name="login"),
    path('registerform/',views.registerform,name="registerform"),
    path('register/',views.register,name="register"),
    path('my_profile/', views.my_profile, name="my_profile"),
    path('profile/', views.profile, name="profile"),
    path('render_profile/', views.render_profile, name="render_profile"),
    path('logout/',views.logout,name="logout"),
    path('mybooking/',views.mybooking,name="mybooking"),
    path('booking/<id>',views.render_book,name="booking"),
    path('booking/',views.render_book_goods,name="booking_goods"),
]