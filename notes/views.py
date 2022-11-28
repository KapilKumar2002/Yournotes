from django.shortcuts import redirect, render
from django.views import View
from .models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    return render(request, "notes/homepage.html")
@login_required
def contact(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        number = request.POST['number']
        email = request.POST['email']
        message = request.POST['message']

        usermessage = Contact(fullname=fullname,mobilenumber=number,email=email,message=message)
        usermessage.save()
        return redirect("/")
    else:
        return render(request, "notes/contact.html")

    