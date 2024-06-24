from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    #login
    path('logout/', views.logout_view, name='logout'),
    #logout
    path('signup/', views.signup_view, name='signup'),
    #registration/signup

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name=''), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

]