from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render


# @login_required(login_url='/')
# @permission_required('core.is_manager', login_url='/auth/login/')


@user_passes_test(lambda u: u.is_manager(), login_url='/auth/login/manager')
def manager_home_view(request):
    # return render(request, 'manager_dashboard/home.html')
    return HttpResponse(f'{request.user.email} is logged in')


@user_passes_test(lambda u: u.is_contractor(), login_url='/auth/login/contractor')
def contractor_home_view(request):
    return render(request, 'dashboard/contractor/home.html')
    # return HttpResponse(f'{request.user.email} is logged in')
