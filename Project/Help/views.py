from django.contrib.auth import logout, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import signUpForm, LoginForm, ApplicationForm
from django.contrib.auth import login as auth_login

from .models import Role, Task, Status
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('home')



def signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            role = Role.objects.get(pk=1)

            user = form.save(commit=False)
            user.role = role
            user.save()
            return redirect('home')
        else:
            messages.error(request, "Произошла ошибка при регистрации.")
    else:
        form = signUpForm()
    return render(request, 'registrations.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect('home')
        else:
            messages.error(request, "Неверный логин/электронная почта или пароль.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def user_applications(request):
    if request.user.is_authenticated:
        applications = Task.objects.filter(user=request.user)
        return render(request, 'applications.html', {'applications': applications})
    else:
        return render(request, 'applications.html')


def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user

            new_status, created = Status.objects.get_or_create(code='new', defaults={'name': 'Новая'})
            application.status = new_status

            application.save()
            return redirect('home')
    else:
        form = ApplicationForm()
    return render(request, 'create_application.html', {'form': form})


def admin_dashboard(request):
    applications = Task.objects.all()
    statuses = Status.objects.all()
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        status_code = request.POST.get('status')
        if application_id and status_code:
            application = get_object_or_404(Task, pk=application_id)

            status = get_object_or_404(Status, code=status_code)

            application.status = status
            application.save()

            return HttpResponseRedirect(request.path_info)

    return render(request, 'admin_dashboard.html', {'applications': applications, 'statuses': statuses})