from django.shortcuts import render
from todolist.models import *
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url='login/')
def todolist(request):
    list_task = Task.objects.filter(user=request.user)
    context = {
        'tasks': list_task,
        'username': request.user,
        'last_login': request.COOKIES['last_login'],
        }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description, date=datetime.date.today(), user=request.user)
        return HttpResponseRedirect(reverse("todolist:todolist")) 
    return render(request, "create_task.html")

@login_required(login_url='login/')
def delete(request, id):
    Task.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse("todolist:todolist"))

@login_required(login_url='login/')
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def create_task_ajax(request):
    if (request.method == 'POST'):
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        date = datetime.date.today()
        task = Task.objects.create(title=title, description=description, date=date, user=user)
        result = {
            'fields':{
                'title':task.title,
                'description':task.description,
                'date':task.date,
            },
            'pk':task.pk
        }
        print(result)
        return JsonResponse(result)

@login_required(login_url='login/')
@csrf_exempt
def delete_task_ajax(request, id):
    if (request.method == 'DELETE'):
        Task.objects.filter(pk=id).delete()
        return HttpResponse(status=202)

