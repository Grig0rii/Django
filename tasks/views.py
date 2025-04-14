from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Task, Category
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    
    # Поиск
    search_query = request.GET.get('search', '')
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Фильтрация по категории
    category_id = request.GET.get('category')
    if category_id:
        tasks = tasks.filter(category_id=category_id)
    
    # Фильтрация по приоритету
    priority = request.GET.get('priority')
    if priority:
        tasks = tasks.filter(priority=priority)
    
    # Фильтрация по статусу
    completed = request.GET.get('completed')
    if completed is not None:
        tasks = tasks.filter(completed=completed == 'true')
    
    categories = Category.objects.all()
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'categories': categories,
        'search_query': search_query,
    })

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Задача успешно создана!')
            return redirect('task_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'categories': Category.objects.all()
    })

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Задача успешно обновлена!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Задача успешно удалена!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
