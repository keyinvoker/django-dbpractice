from django.contrib import messages
from django.shortcuts import render, redirect
from .models import People
from datetime import datetime

# Create your views here.
def index(request):
    people = People.objects.all();
    return render(request, 'index.html', {'people': people})
    
def insert(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        zip = request.POST['zip']
        income = request.POST['income']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if email and People.objects.filter(email=email).exists():
                messages.error(request, 'Email already used!')
                return redirect('insert')
            elif People.objects.filter(name=name).exists():
                messages.error(request, 'Name already exists!')
                return redirect('insert')
            elif People.objects.filter(phone=phone).exists():
                messages.info(request, 'Phone already used!')
                return redirect('insert')
            else:
                people = People.objects.create(name=name, phone=phone, email=email, address=address, city=city, zip=zip, income=income, password=password, updated=False)
                people.save();
                return redirect('index')
        else:
            messages.info(request, 'Password doesn\'t match!')
            return redirect('index')
    else:
        return render(request, 'insert.html')
        
def update(request, pk):
    person = People.objects.get(pk=id)
    
    if request.method == 'POST':
        phone = request.POST['phone']
        email = request.POST['email']
        
        if People.objects.filter(email=email).exists():
            messages.info(request, 'Email already used!')
            return redirect('insert')
        elif People.objects.filter(phone=phone).exists():
            messages.info(request, 'Phone already used!')
            return redirect('insert')
        else:
            people = People.objects.update(phone=phone, email=email)
            people.save();
            return redirect('index')
    else:
        return render(request, 'update.html', {'person': person})

def search(request, pk):
    person = People.objects.get(pk=pk)
    return render(request, 'search.html', {'person': person})