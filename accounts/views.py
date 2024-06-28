from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import EmailAuthenticationForm, CustomUserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetConfirmView

User = get_user_model()

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')    

    if request.method == 'POST':
        form = EmailAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username_or_email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/')  
            else:
                error_message = 'Invalid credentials'
        else:
            error_message = 'Invalid form submission'
    else:
        form = EmailAuthenticationForm()
        error_message = None
        
    context = {'form': form, 'error_message': error_message}
    return render(request, 'accounts/login.html', context)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CustomUserCreationForm()
        
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')