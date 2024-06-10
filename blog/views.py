from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__isnull=False).order_by('-published_date')
    print(kwargs)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        post = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        post = posts.filter(tags__name__in=[kwargs['tag_name']])

   
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Your message has been sent successfully.')
        else:
            messages.add_message(request,messages.ERROR, 'Your message has not been  sent successfully.')
    posts = Post.objects.filter(status=1, published_date__isnull=False).order_by('-published_date')
    post = get_object_or_404(posts, pk=pid)
    comments = Comments.objects.filter(post=post.id, approved=True).order_by('-created_date')
    post.counted_view += 1
    post.save()
    prev_post = Post.objects.filter(published_date__lt=post.published_date, status=1).order_by('-published_date').first()
    next_post = Post.objects.filter(published_date__gt=post.published_date, status=1).order_by('published_date').first()
    form = CommentForm()
    context = {'post': post, 'prev_post': prev_post, 'next_post': next_post, 'comments': comments, 'form': form}
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
    