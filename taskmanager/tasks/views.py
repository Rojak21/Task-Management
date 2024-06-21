from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task


# Create your views here.


# @login_required
def task_list(request):
    tasks =  Task.objects.filter(user = request.user)
    print(type(request.user))
    return render(request, "tasks/task_list.html", {"tasks":tasks})

# @login_required
def task_create (request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user= request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form":form})

# login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# @login_required
def task_delete(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})