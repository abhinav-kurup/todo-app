from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks=task.objects.all()
    form=todoform()

    if request.method == "POST":
        form=todoform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'tasks':tasks,'form':form}
    return render (request,'home.html',context)

def update(request,pk):
    tasks = task.objects.get(id=pk)
    form = todoform(instance=tasks)
    if request.method == "POST":
        form=todoform(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request,'update.html',context)

def delete(request,pk):
    tasks = task.objects.get(id=pk)
    if request.method == "POST":
        tasks.delete()
        return redirect('/')
    context = {'tasks':tasks}
    return render(request,'delete.html',context)