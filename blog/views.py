from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now, status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now, status=1)
    post = get_object_or_404(posts, pk=pid)
    post.counted_view += 1
    post.save()
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)


# def test(request, name, family_name, age):
def test(request, pid):
    # context = {'name': name, 'family_name': family_name, 'age': age}
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'test.html', context)
