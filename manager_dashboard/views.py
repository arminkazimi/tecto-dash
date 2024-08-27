from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='/auth/login/')
# @permission_required('core.manager')
def homeView(request):
    # return render(request, 'manager_dashboard/home.html')
    return HttpResponse(f'{request.user.email} loged in')
