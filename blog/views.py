from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    print(kwargs)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        post = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 3)

    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    post.counted_view += 1
    post.save()
    
    prev_post = Post.objects.filter(id__lt=post.pk, status=1).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=post.pk, status=1).order_by('id').first()

    context = {'post': post, 'prev_post': prev_post, 'next_post': next_post}

    return render(request, 'blog/blog-single.html', context)


# def test(request, name, family_name, age):
def test(request):
    # context = {'name': name, 'family_name': family_name, 'age': age}
    # post = Post.objects.get(id=pid)
    # post = get_object_or_404(Post, pk=pid)
    # context = {'post': post}
    return render(request, 'test.html')

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    #print(request.__dict__)
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        # print(request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
    