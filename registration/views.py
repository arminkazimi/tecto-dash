from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse

from core.models import CustomUser
from .forms import CustomLoginForm


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = self.kwargs['user_type']

        return context

    def get_default_redirect_url(self):
        user = self.request.user
        if user.type == CustomUser.Types.MANAGER:
            return reverse('manager-home')
        elif user.type == CustomUser.Types.CONTRACTOR:
            return reverse('contractor-home')



