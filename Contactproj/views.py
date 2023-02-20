from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here. 



def index(request):
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

            new_contact = Contact.objects.create(full_name=full_name, relationship=relationship, phone_number=phone_number, email=email, address=address)
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

