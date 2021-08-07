from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CustomRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method=='POST':
        register_form=CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("Your Account Created Succesfully,Pls Login to get Started !"))
            return redirect('register')


    else:
        register_form=CustomRegisterForm()

    return render(request,'register.html',{'register_form':register_form})
@login_required
def theoryhome(request):
    context={
    'welcome':'contact'
    }
    return render(request,'theoryhome.html',context)
@login_required
def theory(request,type,value):
    context={
    'welcome':'contact'
    }
    if type=='python':
        if value==1:
            return render(request,'python1.html',context)
        if value==2:
            return render(request,'python2.html',context)
        if value==3:
            return render(request,'python3.html',context)
        if value==4:
            return render(request,'python4.html',context)
        if value==5:
            return render(request,'python5.html',context)
        if value==6:
            return render(request,'python6.html',context)
    if type=='java':
        if value==1:
            return render(request,'java1.html',context)
        if value==2:
            return render(request,'java2.html',context)
        if value==3:
            return render(request,'java3.html',context)
        if value==4:
            return render(request, 'java4.html',context)
        if value==5:
            return render(request,'java5.html',context)
        if value==6:
            return render(request,'java6.html',context)
