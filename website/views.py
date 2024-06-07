from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from blog.models import Post
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = "Unknown"
            contact.save()
            messages.add_message(request,messages.SUCCESS, 'Your message has been sent successfully.')
        else:
            messages.add_message(request,messages.ERROR, 'Your message has not been sent.')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def elements_view(request):
    return render(request, 'website/elements.html')

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # subject = form.cleaned_data['subject']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # print(name, subject, email, message)
            return HttpResponse('done')
        else:
            return HttpResponse('not done')
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')
        # c = Contact()
        # c.name = name
        # c.email = email
        # c.subject = subject
        # c.message = message
        # c.save()
    form = ContactForm()
    return render(request, 'test.html', {'form': form})
        
def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    