from django.urls import path
from website.views import *

app_name = 'website'
urlpatterns = [
    path('',index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('elements', elements_view, name='elements'),
    path('test/', test_view, name='test'),
    path('newsletter', newsletter_view, name='newsletter'),
    # path('', coming_soon, name='coming_soon'),
    # path('<path:resource>/', coming_soon, name='coming_soon'),

]
