from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User 
from ilan.models import Advert
# Create your views here.
def index(request):
    context = dict()
    advert = Advert.objects.all()
    context["advert"] = advert
    return render(request,"kullanici/index.html",context)

def profil(request):
    context = dict()
    context["user_profil"] = User.objects.filter(username=request.user)
    return render(request,"kullanici/profil.html",context)

def profil_update(request,id):
    user = User.objects.filter(id =id)
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    username = request.POST["username"]
    phone = request.POST["phone"]
    email = request.POST["email"]
    is_Employer= request.POST.get("isEmployer",False)
    if is_Employer == "on":
        is_Employer = True
        isEmployer = is_Employer
    else:
        isEmployer = request.POST.get("isEmployer",False)
    user.update(email=email,first_name=firstname,last_name=lastname,username=username,phone=phone,isEmployer=isEmployer)
    return render(request,"kullanici/profil.html")

def password(request):
    return render(request,"kullanici/password.html")
def password_change(request,id):
    if request.method == 'POST':
        user_password = request.POST["password"]
        user = User.objects.get(id = id)
        user.set_password(user_password)
        user.save()
        return render(request,"login/login.html")
    return render(request,"kullanici/password.html")