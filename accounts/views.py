from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def home(request):
    if request.method =="POST":#did the user submit the form?if yes, continue, if no, show the login page
        username= request.POST.get("username")
        password=request.POST.get("password")
        
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "accounts/login.html")

    return HttpResponse(f"username: {username}<br>Password: {password}")
    return render(request,"accounts/login.html")
def register(request):

    if request.method =="POST":
        first_name= request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email = request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        if password1 != password2:
          messages.error(request, "Passwords do not match.")
          return render(request, "accounts/register.html") 
        
        if User.objects.filter(username=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, "accounts/register.html")
        
        
        
        user = User.objects.create_user(
          username=email,
          email=email,
          first_name=first_name,
          last_name=last_name,
          password=password1,
          
)

        user.save()
  
        messages.success(request, "Account created successfully!")

        return redirect("login")
    return render(request,"accounts/register.html")
def dashboard(request):
    return render(request,"accounts/dashboard.html")
def reset(request):
    return render(request,"accounts/reset.html")




