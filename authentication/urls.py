from django.urls import path,re_path
from . import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('register',views.register , name = 'register'),
    path('login',views.login , name = 'login'),
    path('logout',views.logout , name = 'logout'),
    path('dash', views.dash , name = 'dash' ) ,
    re_path(r'specialaccess/[0-9 A-Z a-z]+' , views.specialuser , name = 'specialuser' ),
    re_path(r'showrequests/[0-9 A-Z a-z]*' , views.show_requests , name = 'show_requests' ),
    re_path(r'giveaccess/[0-9 A-Z a-z]+/*' , views.give_access , name = 'give_access'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
]