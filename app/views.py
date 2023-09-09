from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse

def insert_marvel(request):
    MFEO = MarvelForm()
    d = {'MFEO':MFEO}

    if request.method == "POST":
        MFDO =  MarvelForm(request.POST)
        if MFDO.is_valid():
            mname = MFDO.cleaned_data['mname']
            mid = MFDO.cleaned_data['mid']
            mlan = MFDO.cleaned_data['mlan']  


            mo = Marvel.objects.get_or_create(mname=mname,mid=mid,mlan=mlan)[0]
            mo.save()

            MA = Marvel.objects.all()
            d1 ={'MA':MA} 
            return render(request,'display_marvel.html',d1)

    return render(request,"insert_marvel.html",d)