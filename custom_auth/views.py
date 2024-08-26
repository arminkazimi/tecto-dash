from django.shortcuts import render


def login(request):
    return render(request, "my_auth/login.html")
