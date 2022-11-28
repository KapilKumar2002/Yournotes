from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def Studentlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("/accounts/Studentlogin/")
    else:
        return render(request, "accounts/login.html")
def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username already taken!")
                return render(request, "accounts/register.html")
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email already taken!")
                return render(request, "accounts/register.html")
            else:
                user = User.objects.create_user(username=username, email=email,first_name = firstname, last_name=lastname,password=password1)
                user.save()
                messages.info(request, "Your account successfully created")
                return  redirect("/accounts/Studentlogin/")
        else:
            return render(request, "accounts/register.html")
    else:
        return render(request, "accounts/register.html")

def logout(request):
    auth.logout(request)
    return redirect("/")