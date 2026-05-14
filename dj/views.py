from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("This is home page")
    people = [
        {
            "name": "Alice Johnson", "age": 28, "city": "New York"
        },
        {
            "name": "Bob Smith", "age": 34, "city": "Chicago"
        },
        {
            "name": "Charlie Brown", "age": 22, "city": "San Francisco"
        },
        {
            "name": "Diana Prince", "age": 29, "city": "Los Angeles"
        },
        {
            "name": "Sam Parker", "age": 25, "city": "Maryland"
        }
    ]
    context = {
        "title": "Home Page",
        "body": "Welcome to Home page",
        "people": people
    }
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse("This is about us page")
    content = {
        "title": "About Us Page",
        "body": " Welcome to About Us page"
    }
    return render(request, 'about.html', content)

def phone(request):
    # return HttpResponse("This is contact page")
    phone = [
        {
            "phone": 123
        },
    ]
    content = {
        "title": "Contact Page",
        "body": "Welcome to Phone Page",
        "phone": phone
    }
    return render(request, 'phone.html', content)

def email(request):
    # return HttpResponse("This is contact page")
    email = [
        {
            "email": "abc@gmail.com"
        },
    ]
    content = {
        "title": "Contact Page",
        "body": "Welcome to Email Page",
        "email": email
    }
    return render(request, 'email.html', content)

def address(request):
    # return HttpResponse("This is contact page")
    address = [
        {
            "address": "ktm"
        },
    ]
    content = {
        "title": "Contact Page",
        "body": "Welcome to Address Page",
        "address": address
    }
    return render(request, 'address.html', content)