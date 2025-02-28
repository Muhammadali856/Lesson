from django.shortcuts import render
from users.forms import RegisterForm, LoginForm
import threading
from users.utils import send_email_confirmation
from users.models import CustomUserModel
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.contrib.auth import authenticate, login


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(raw_password=request.POST['password1'])
            user.save()
            
            email_thread = threading.Thread(target=send_email_confirmation, args=(request, user))
            email_thread.start()
            return render(request, template_name='auth/check_email.html')
    else:
        return render(request, template_name='auth/register.html')


def confirm_email_view(request, vid, token):
    try:
        user = CustomUserModel.objects.get(id=vid)
    except CustomUserModel.DoesNotExist:
        messages.error(request, 'User nor found')
        return redirect('users:register')
    
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, template_name='auth/email_confirmed.html')
    else:
        messages.error(request, 'Invalid token')
        return redirect('users:register') 


    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_username = request.POST['email_or_username']
            password = request.POST['password']

            try:
                user = CustomUserModel.objects.get(
                    Q(email=email_or_username) | Q(username=email_or_username)
                )
            except CustomUserModel.DoesNotExist:
                messages.error(request, 'User nor found')
                return redirect('users:register')
            
            authenticated_user = authenticate(username=user.usernname, password=password)
            if authenticated_user is not None:
                login(request, user)
                return redirect('pages:home')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('users:login')
    else: 
        return render(request, template_name='users/login.html')
