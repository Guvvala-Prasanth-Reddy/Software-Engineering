from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('register',views.register , name = 'register'),
    path('login',views.login , name = 'login'),
    path('logout',views.logout , name = 'logout'),
    path('dash', views.dash , name = 'dash' ) ,
    re_path(r'specialaccess/[0-9 A-Z a-z]+' , views.specialuser , name = 'specialuser' ),
    re_path(r'showrequests/[0-9 A-Z a-z]*' , views.show_requests , name = 'show_requests' ),
    re_path(r'giveaccess/[0-9 A-Z a-z]+/[0-9 A-Z a-z]+/' , views.give_access , name = 'give_access'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    path('password-reset',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password-reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),


]