from django.urls import path
from . import views
urlpatterns=[
    path("profile",views.profileInfo,name='profileInfo'),
    path("base",views.base,name='base'),
    path("register",views.register,name='register'),
    path("new",views.newPage,name='newpage'),
    path("bookNew",views.bookNew,name='bookNew'),
    path("test",views.test,name='test'),
    path("login",views.login,name='login'),
    path("loginCheck",views.loginCheck,name='loginCheck'),
    path("about",views.about_us,name='about_us'),
    path("bill",views.bill,name='bill'),
    path("booking",views.booking,name='booking'),
    path("contact-us",views.contact_us,name='contact_us'),
    path("serviceEasy.com",views.index,name='index'),
    path("home",views.index_loggedin,name='index_loggedin'),
    path("404",views.fourOHfour,name='fourOHfour'),
    path("upcoming",views.coming_soon,name='coming_soon'),
    path("registerProvider",views.registerProvider,name='registerProvider'),





]