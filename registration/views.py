from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from core.models import CustomUser
from .forms import CustomLoginForm


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'

    # success_url = reverse_lazy('manager-home')
    def get_success_url(self):
        user = self.request.user
        print(user)
        if user.type == CustomUser.Types.MANAGER:
            # Replace with the actual name of your manager dashboard view
            print(reverse('manager-home'))
            return reverse('manager-home')
        elif user.type == CustomUser.Types.CONTRACTOR:
            # Replace with the actual name of your contractor dashboard view
            print(reverse('contractor-home'))
            # success_url = reverse('contractor-home')
            return reverse('contractor-home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = self.request.GET.get('user_type', None)
        return context


@login_required
def check_user_view(request):
    user = request.user
    print(user, 'in check user')
    return HttpResponse('hi')
    if user.type == CustomUser.Types.MANAGER:
        # Replace with the actual name of your manager dashboard view
        # print(reverse('manager-home'))

        return redirect('manager-home')
    elif user.type == CustomUser.Types.CONTRACTOR:

        return redirect('contractor-home')
# def get_success_url(self):
#     user = self.request.user
#     print(user)
#     if user.type == CustomUser.Types.MANAGER:
#         # Replace with the actual name of your manager dashboard view
#         print(reverse('manager-home'))
#         success_url = reverse('manager-home')
#     elif user.type == CustomUser.Types.CONTRACTOR:
#         # Replace with the actual name of your contractor dashboard view
#         print(reverse('contractor-home'))
#         success_url = reverse('contractor-home')
# def form_valid(self, form):
#     response = super().form_valid(form)
#     user = form.get_user()
#
#     if user.type == CustomUser.Types.MANAGER:
#         # Replace with the actual name of your manager dashboard view
#         self.success_url = reverse_lazy('manager-home')
