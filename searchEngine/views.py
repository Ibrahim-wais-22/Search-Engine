from django.contrib.auth.forms import UserModel
from django.shortcuts import redirect, render
from .forms import AddForm
from .models import Crawl_tb ,AddCommint
from django.contrib.auth.models import User


def home(request):
    return render(request,'searchEngine/index.html' )


  
def result1(request):
    quere = Crawl_tb.objects.all()
    name = request.GET['q']
    if name: 
        
        quere = quere.filter(title__icontains=name)
        
        # quere1 = quere.filter(discraption__icontains=name)
        context = {
            'title':quere,
            'name':name
        }      
        
        return render(request,'searchEngine/list_pages.html',context)
    elif name !=True:
        return render(request,'searchEngine/error.html')
    elif quere == []:
        return render(request,'searchEngine/error.html')


def go(request):
    go = Crawl_tb.objects.all()
    context = {
            'go':go,
        }
    
    return render(request,'searchEngine/list_pages.html',context)
    
    


def add(request):
    # form = AddForm()

    if request.method=="GET":
        form = AddForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/searchEngine/')
    else:    
        form = AddForm()
    
    return render(request,'searchEngine/add.html',{'form':form})





def dashboard(request):
    quere = Crawl_tb.objects.all()
    quere2 = User.objects.all()
    addcomment = AddCommint.objects.all()
    context = {
            'title2':quere,
            'admins':quere2,
            'adds':addcomment,
        }
    return render(request,'searchEngine/dashboard.html',context)
