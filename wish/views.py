from django.shortcuts import render,redirect
from wish.models import wishlist

# Create your views here.


def home(request):
    return render(request,'home.html')

def details(request):
    qry_wish=wishlist(name=request.POST['t1'],wish=request.POST['t2'],date=request.POST['t3'])
    qry_wish.save()
    return redirect('/')

def display(request):
    display_qry=wishlist.objects.all()
    return render(request,'display.html',{'qry1':display_qry})

