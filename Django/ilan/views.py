from django.shortcuts import render
from ilan.models import Advert 
import datetime
# Create your views here.
def add_advert(request):
    if request.method == 'POST':
        advert_name = request.POST["advert_name"]
        advert_desc = request.POST["advert_desc"]
        advert_city = request.POST["advert_city"]
        advert_company = request.POST["advert_company"]
        advert_experience = request.POST["advert_experience"]
        education_level = request.POST["education_level"]
        advert= Advert.objects.create(advert_date=datetime.date.today(), advert_name=advert_name,advert_desc=advert_desc,advert_city=advert_city,advert_company=advert_company,advert_experience=advert_experience,education_level=education_level)
        advert.save()
        return render(request,"kullanici/index.html")
    return render(request,"advert/add_advert.html")

def search_advert(request):
    if request.method == 'POST':
        print("posteldlsdkşjflsdjkfslkdjfskldfjklsdf")
        keyword = request.POST["keyword"]
        print(keyword , "anananananannananannnannannana")
        adverts = Advert.objects.filter(advert_name__icontains = keyword)
        context = dict()
        context["advert"] = adverts
        return render(request,"kullanici/index.html",context)
    print("asdasdasdasd")
    return render(request,"kullanici/index.html")