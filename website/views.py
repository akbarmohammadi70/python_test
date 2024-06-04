from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages

app_name='website'
def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():  
    #         name = form.cleaned_data['name']
    #         name = 'ناشناس'
    #         form.save()
    #         messages.add_message(request, messages.SUCCESS, 'Your ticket submited successfully...')
    #     else:
    #         messages.add_message(request, messages.ERROR, 'Your ticket did not submited...')
    # form = ContactForm()
    # return render(request, 'website/contact.html', {'form': form})
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if name == 'علی':
                form.instance.name = 'ناشناس'
            messages.add_message(request, messages.SUCCESS, 'Your ticket submited successfully...')
            form.save()

        else:
            messages.add_message(request, messages.ERROR, 'Your ticket did not submited...')


        # c.save()
        # print(c.name)
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})
            

def elements_view(request):
    return render(request, 'website/elements.html')

def test_view(request):
    if request.method == 'POST':
    #    name = request.POST.get('name')
    #    email = request.POST.get('email')
    #    subject = request.POST.get('subject')
    #    message = request.POST.get('message')
    #    c = Contact()
    #    c.name = name
    #    c.email = email
    #    c.subject = subject
    #    c.message = message
    #    c.save()
    #    print(name)
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # subject = form.cleaned_data['subject']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # print(name, subject, email, message)
            name = form.cleaned_data['name']
            name = 'Unknown'
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('Not Valid')
    
    form = ContactForm()
    return render(request, 'test.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = 'Unknown'
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

########


# def coming_soon(request):
#     return render(request, 'coming_soon.html')


        
