from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User 

def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        is_Employer= request.POST.get("isEmployer",False)
        if is_Employer == "on":
            is_Employer = True
            isEmployer = is_Employer
        else:
            isEmployer = request.POST.get("isEmployer",False)
        if User.objects.filter(username=username).exists():
            print( "username"+ username +"email"+email+ "password"+password+
            "isEmployer"+isEmployer+
            "firstname"+firstname+
            "lastname"+lastname)
            return render(request,"login/register.html",{ "error":"kullanıcı adı zaten var", })
        else:
            if User.objects.filter(email=email).exists():
                return render(request,"login/register.html",{"error":"mail adresi kullanılıyor."})
            else:
                user = User.objects.create_user(email=email,first_name=firstname,last_name=lastname,username=username,isEmployer=isEmployer,password=password)
                user.save()
                return redirect("login")
    return render(request,"login/register.html")

    
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect("anasayfa")
        else:
            print(username,password)
            return render(request,"login/login.html",{
                "error":"kullanıcı adı veya şifre hatalı"
            })
    return render(request,"login/login.html")


def logout(request):
    auth_logout(request)
    return redirect("anasayfa")