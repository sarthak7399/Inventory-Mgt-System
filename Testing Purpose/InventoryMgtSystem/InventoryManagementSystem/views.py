from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    # return HttpResponse("Hello, world. You're at the InventoryManagementSystem index.")
    return render(request, "index.html")

def signup(request):

    if(request.method=="POST"):
        # username = request.POST.get('username') OR
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        myUser = User.objects.create(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
        myUser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect("login")

    return render(request, "authentication/signup.html")

def login(request):

    if (request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if(user is not None):
            login(request, user)
            return render(request, "index.html", {"firstname": user.first_name})
        else:
            messages.error(request, "Invalid credentials, please try again")
            return redirect("home")
        
    return render(request, "authentication/login.html")

def logout(request):
    return render(request, "index.html")
