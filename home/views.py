from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TaskForm, TaskListForm
from .models import TaskList, Task
from django.core.mail import send_mail
from accounts.forms import ResetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from django.core.signing import TimestampSigner
from accounts.views import login

def task_lists(request):
    todolists = TaskList.objects.filter(user=request.user)
    context = {'todolists': todolists, 'request':request}
    return render(request, 'index.html', context)

def task_list_detail(request, pk):
    todolist = get_object_or_404(TaskList, pk=pk)
    todolists = TaskList.objects.filter(user=request.user)
    tasks = Task.objects.filter(task_list=todolist)
    context = {'todolist': todolist, 'todolists': todolists, 'tasks': tasks , 'pk': pk}
    return render(request, 'tasks.html', context)

def task_list_new(request):
    if request.method == "POST":
        form = TaskListForm(request.POST)
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.user = request.user
            task_list.save()
            messages.success(request, 'TaskList created successfully', 'success')
            return redirect('task_list_detail', pk=task_list.pk)
    else:
        form = TaskListForm()
    return render(request, 'task_list_edit.html', {'form': form})

def task_list_edit(request, pk):
    task = get_object_or_404(TaskList, pk=pk)
    if request.method == "POST":
        form = TaskListForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            messages.success(request, 'Task List edited successfully', 'success')
            return redirect('task_list_detail', pk=task.pk)
    else:
        form = TaskListForm(instance=task)
    return render(request, 'task_list_edit.html', {'form': form})

def task_list_delete(request, pk):
    task_list = get_object_or_404(TaskList, pk=pk)
    task_list.delete()
    messages.success(request, 'Task List deleted successfully', 'success')
    return redirect('task_lists')

def task_new(request, pk):
    task_list = get_object_or_404(TaskList, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_list = task_list
            task.save()
            messages.success(request, 'Task created successfully', 'success')
            return redirect('task_list_detail', pk=task_list.pk)
    else:
        form = TaskForm()
    return render(request, 'task_edit.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            messages.success(request, 'Task edited successfully', 'success')
            return redirect('task_list_detail', pk=task.task_list.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task_list_pk = task.task_list.pk
    task.delete()
    messages.success(request, 'Task deleted successfully', 'success')
    return redirect('task_list_detail', pk=task_list_pk)

def forget_password(request):
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = get_object_or_404(User, email=cd['email'])
            email = cd['email']
            signer = TimestampSigner()
            signed_value = signer.sign(user.username)
            if user is not None:
                subject = 'Password Reset'
                html_message = render_to_string('password_email.html', {'value': signed_value})
                plain_message = strip_tags(html_message)
                to = email
                mail.send_mail(subject, plain_message, '', [to], html_message=html_message)
                return render(request, 'confirm_password.html', {'email': email})
            else:
                return render(request, 'confirm_password.html', {'email': email})
    else:
        form = ResetPasswordForm()
        return render(request, 'forget_password.html', {'form': form})
    
def change_password(request, signed_value):
    signer = TimestampSigner()
    unsigned_value = signer.unsign(signed_value, max_age=600)
    username = str(unsigned_value)
    user = User.objects.get(username=username)
    if user is not None:
        if request.method == "POST":
            form = PasswordChangeForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                if cd['password'] == cd['confirmpassword']:
                    user.set_password(cd['password'])
                    user.save()
                    messages.success(request, 'Password changes successfully', 'success')
                    return redirect('login')
                else:
                    messages.error(request, 'These passwords dont match. Try again!', 'danger')
        else:
            form = PasswordChangeForm()
        return render(request, 'change_password.html', {'form': form})