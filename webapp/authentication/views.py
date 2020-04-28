from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import  force_bytes,force_text,DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.views import View


# Create your views here.

def home(request):
    return render(request,'index.html')

def dash(request):
    return render(request, 'dash.html')


def login(request):
    if( request.method == 'POST'):
        username    = request.POST['uname']
        password    = request.POST['pass']
        user        = auth.authenticate(username=username,password=password)
        if( user is not None):
            if user.is_active:
                auth.login(request,user)
                return redirect('dash')
            else:
                messages.info(request,'Please verify your email')
                return redirect('login')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if( request.method == 'POST'):
        first_name  = request.POST['fname']
        last_name   = request.POST['lname']
        username    = request.POST['uname']
        email       = request.POST['email']
        password    = request.POST['pass']
        password1   = request.POST['pass1']
        if( password == password1):
            if( User.objects.filter(username=username).exists()):
                messages.info(request,'user name exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username , password = password1 , email = email , first_name = first_name , last_name = last_name,is_active=False)
                user.save()
                current_site=get_current_site(request)
                email_subject='Activate your Adharva Account'
                message=render_to_string('activate_account.html',
                {
                    'user':user,
                    'domain':current_site,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':generate_token.make_token(user)
                }
                )

                email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
                email_message.send()
                messages.info(request,'Activation link is sent to your registered email')
                return redirect('login')
        else:
            messages.info(request,'passwds dsnt match')
            return redirect('register')
    else:
        return render(request,'register.html')




class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,'Account Activated Successfully')
            return redirect('login')

        return render(request,'activation_failed.html',status=401)