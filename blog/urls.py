from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed


app_name = 'blog'
urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('tag/<str:tag_name>', blog_view, name='tag'),
    path('author/<str:author_username>', blog_view, name='author'),
    # path('<str:name>/lastname/<str:family_name>/age/<int:age>' ,test, name='test'),
    path('search/', blog_search, name='search'),
    path("rss/feed/", LatestEntriesFeed()),

    # path('test' ,test, name='test'),


]
