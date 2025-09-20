from django.shortcuts import render, redirect
from django.contrib import messages
from myapp.models import Message

# Create your views here.
def index(request):
    if request.method == "POST":
        mymessage = Message(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mymessage.save()
        messages.success(request, 'Your message has been sent successfully! Thank you for contacting us.')
        return redirect('index')

    else:
        return render(request, 'index.html')
       
def about(request):
    return render(request, 'about.html' )

def services(request):
    return render(request, 'services.html' )

def contact(request):
    if request.method == "POST":
        mymessage = Message(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mymessage.save()
        messages.success(request, 'Your message has been sent successfully! Thank you for contacting us.')
        return redirect('/contact.html')

    else:
        return render(request, 'contact.html')
    

def FAQs(request):
    return render(request, 'FAQs.html' )

def projects(request):
    return render(request, 'projects.html' )

def testimonials(request):
    return render(request, 'testimonials.html' )


        
    
   