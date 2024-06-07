from django import template
from blog.models import Post
from django.utils import timezone


register = template.Library()


@register.inclusion_tag('website/latest_posts.html')
def latest_posts(count=6):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')[:count]
    return {'latest_posts': posts}

