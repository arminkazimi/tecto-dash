from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse
from django.shortcuts import render


# @login_required(login_url='/auth/login/')
# @permission_required('core.contractor')
def homeView(request):
    # return render(request, 'contractor_dashboard/home.html')
    return HttpResponse(f'{request.user.email} loged in')

