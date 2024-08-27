from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import ManagerLoginForm


# Custom login view for Managers
def manager_login(request):
    if request.method == 'POST':
        form = ManagerLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                # Get the manager by email
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            # Authenticate using the user found by email
            if user is not None and user.is_manager and user.check_password(password):
                login(request, user)
                return redirect('manager_home')  # Redirect to the manager home page
            else:
                form.add_error(None, 'Invalid manager email or password')
    else:
        form = ManagerLoginForm()
    # Render the manager login form template
    return render(request, 'registration/manager_login.html', {'form': form})


# Custom login view for teachers
def teacher_login(request):
    if request.method == 'POST':
        form = TeacherEmailLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                # Get the teacher by email
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            # Authenticate using the user found by email
            if user is not None and user.is_teacher and user.check_password(password):
                login(request, user)
                return redirect('teacher_home')  # Redirect to the teacher home page
            else:
                form.add_error(None, 'Invalid teacher email or password')
    else:
        form = TeacherEmailLoginForm()
    # Render the teacher login form template
    return render(request, 'registration/teacher_login.html', {'form': form})
