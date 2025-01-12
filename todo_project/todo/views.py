from django.shortcuts import render, redirect
from .models import Task 
from .forms import TaskForm
from django.shortcuts import get_object_or_404

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Bind data to the form
        if form.is_valid():
            form.save()  # Save the task to the database
            return redirect('task_list')  # Redirect to the task list
    else:
        form = TaskForm()  # Create an empty form
    return render(request, 'add_task.html', {'form': form})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Fetch the task by its ID
    task.completed = True  # Mark the task as completed
    task.save()  # Save the change to the database
    return redirect('task_list')  # Redirect back to the task list

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Fetch the task by its ID
    task.delete()  # Delete the task from the database
    return redirect('task_list')  # Redirect back to the task list