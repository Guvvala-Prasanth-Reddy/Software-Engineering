from django.urls import path,re_path
from . import views

urlpatterns = [  re_path(r'ECE|CSE|MECH|EEE/\d/' , views.courselist , name = 'courselist') ,
                 re_path(r'Adddata\?*' , views.create_content , name = 'create_content' ),
                 re_path(r'give/NT|QP|TB\?*' , views.show_content , name = 'show_content'),
                 re_path(r'[0-9a-zA-Z-_]+.pdf', views.generate_pdf , name = 'generate_pdf'), 

]