from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here. 


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('signin')
        else:
            messages.info(request, 'Password Does Not Match')
            return redirect('signup')
    return render(request, 'signup.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')

    return render(request, 'signin.html')


@login_required(login_url='signup')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Contact.objects.filter(user = user_object)

    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains = search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'index.html', {'contacts':contacts, 'search_input':search_input})



def AddContact(request):
    if request.method == 'POST':
        full_name = request.POST['fullname']
        relationship = request.POST['relationship']
        phone_number = request.POST['phone-number']
        email = request.POST['email']
        address = request.POST['address']

        user_object = User.objects.get(username=request.user.username)
        # user_profile = Contact.objects.get()
        new_contact = Contact.objects.create(user = user_object, full_name=full_name, relationship=relationship, phone_number=phone_number, email=email, address=address)
        new_contact.save() 
        return redirect('/')
        

    return render(request, 'new.html')



def EditContact(request,pk):
    edit_contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        edit_contact.full_name = request.POST['fullname']
        edit_contact.relationship = request.POST['relationship']
        edit_contact.phone_number = request.POST['phone-number']
        edit_contact.email = request.POST['e-mail']
        edit_contact.address = request.POST['address']

        edit_contact.save()
        return redirect('/profile/' + str(edit_contact.id))

    return render(request, 'edit.html', {'edit_contact':edit_contact})



def ContactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'profile.html', {'contact':contact})



def DeleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')

    return render(request, 'delete.html', {'contact':contact})

