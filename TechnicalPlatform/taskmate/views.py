from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
    if request.method=='POST':
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manager=request.user
            instance.save()
        messages.success(request,('Task Added Successfully'))
        return redirect('todolist')

    else:
        alltasks=TaskList.objects.filter(manager=request.user)
        paginator=Paginator(alltasks,4)
        page=request.GET.get('pg')
        alltasks=paginator.get_page(page)

        return render(request,'todolist.html',{'alltasks':alltasks})



def contact(request):
    context={
    'welcome':'contact'
    }
    return render(request,'contact.html',context)

def privacy(request):
    context={
    'welcome':'contact'
    }
    return render(request,'privacy.html',context)
def refund(request):
    context={
    'welcome':'contact'
    }
    return render(request,'refund.html',context)
def faqs(request):
    context={
    'welcome':'contact'
    }
    return render(request,'faq.html',context)
def terms(request):
    context={
    'welcome':'contact'
    }
    return render(request,'termsofuse.html',context)


def index(request):
    context={
    'welcome':'about'
    }
    return render(request,'index.html',context)

@login_required
def delete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manager==request.user:
        task.delete()
    else:
        messages.error(request,("Access Restricted ,You are not allowed to access this page !"))
    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method=='POST':
        task=TaskList.objects.get(pk=task_id)
        form=TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,('Task Edited Successfully'))
        return redirect('todolist')

    else:
        task_obj=TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})


@login_required
def complete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manager==request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,("Access Restricted ,You are not allowed to access this page !"))
    return redirect('todolist')

@login_required
def pending_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manager==request.user:
        task.done=False
        task.save()
    else:
        messages.error(request,("Access Restricted ,You are not allowed to access this page !"))
    return redirect('todolist')
