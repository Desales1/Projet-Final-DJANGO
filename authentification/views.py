from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from myproject import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from . tokens import generateToken
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# Create your views here.


def home(request, *args, **kwargs):
    return render(request, 'authentification/index.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpwd = request.POST['comfirmpwd']
        if User.objects.filter(username=username):
            messages.error(request, 'username already taken please try another.')
            return redirect('authentification:signup')
        if User.objects.filter(email=email):
            messages.error(request, 'This email has an account.')
            return redirect('authentification:signup')
        if len(username)>10:
            messages.error(request, 'Please the username must not be more than 10 character.')
            return redirect('authentification:signup')
        if len(username)<5:
            messages.error(request, 'Please the username must be at leat 5 characters.')
            return redirect('authentification:signup')
        if not username.isalnum():
            messages.error(request, 'username must be alphanumeric')
            return redirect('authentification:signup')

        if password != confirmpwd:
            messages.error(request, 'The password did not match! ')  
            return redirect('authentification:signup')                  

        my_user = User.objects.create_user(username, email, password)
        my_user.first_name =firstname
        my_user.last_name = lastname
        my_user.is_active = False
        my_user.save()
        messages.success(request, 'Your account has been successfully created. we have sent you an email You must comfirm in order to activate your account.')
# send email when account has been created successfully
        subject = "Welcome to django-application donaldPro"
        message = "Welcome "+ my_user.first_name + " " + my_user.last_name + "\n thank for chosing Dprogrammeur website for test login.\n To order login you need to comfirm your email account.\n thanks\n\n\n donald programmeur"
        
        from_email = settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)

# send the the confirmation email
        current_site = get_current_site(request) 
        email_suject = "confirm your email DonaldPro Django Login!"
        messageConfirm = render_to_string("emailConfimation.html", {
            'name': my_user.first_name,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': generateToken.make_token(my_user)
        })       

        email = EmailMessage(
            email_suject,
            messageConfirm,
            settings.EMAIL_HOST_USER,
            [my_user.email]
        )

        email.fail_silently = False
        email.send()
        return redirect('authentification:signin')
    return render(request, 'authentification/signup.html')    


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        my_user = User.objects.get(username=username)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, 'authentification/index.html', {"firstname":firstname})
        elif my_user.is_active == False:
            messages.error(request, 'you have not confirm your  email do it, in order to activate your account')  
            return redirect('authentification:signin')  
        else:
            messages.error(request, 'bad authentification')
            return redirect('myapp:index4') 

    return render(request, 'authentification/signin.html')    

def signout(request):
    logout(request)
    messages.success(request, 'logout successfully!')
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None

    if my_user is not None and generateToken.check_token(my_user, token):
        my_user.is_active  = True        
        my_user.save()
        messages.success(request, "You are account is activated you can login by filling the form below.")
        return redirect("authentification:signin")
    else:
        messages.success(request, 'Activation failed please try again')
        return redirect('home')
