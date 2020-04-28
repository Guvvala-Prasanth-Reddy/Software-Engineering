from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('register',views.register , name = 'register'),
    path('login',views.login , name = 'login'),
    path('logout',views.logout , name = 'logout'),
    path('dash', views.dash , name = 'dash' ) ,
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),

]