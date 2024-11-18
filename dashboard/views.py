from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView

from dashboard.forms import (
    ProjectForm,
    CrewFormset,
)
from dashboard.models import Project


class CreateProjectView(UserPassesTestMixin, CreateView):
    template_name = 'dashboard/contractor/project-create.html'
    model = Project
    form_class = ProjectForm  # the parent object's form

    def test_func(self):
        return self.request.user.is_contractor()

    def handle_no_permission(self):
        return redirect_to_login(
            self.request.get_full_path(),
            reverse('login', kwargs={'user_type': 'contractor'}),
            'next'
        )

    # On successful form submission
    def get_success_url(self):
        return reverse('project-created')

    # Validate forms
    def form_valid(self, form):
        ctx = self.get_context_data()
        formset = ctx['formset']
        print(form.is_valid())
        print(formset.is_valid())
        print(formset.errors)
        if formset.is_valid() and form.is_valid():
            # saves Father and Children
            self.object = form.save(commit=False)
            self.object.creator = self.request.user
            self.object.save()
            # self.object = project
            for crew_form in formset:
                crew = crew_form.save(commit=False)
                crew.project = self.object
                # crew.project = project
                crew.save()

            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    # We populate the context with the forms. Here I'm sending
    # the inline forms in `inlines`
    def get_context_data(self, **kwargs):
        ctx = super(CreateProjectView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = ProjectForm(self.request.POST)
            ctx['formset'] = CrewFormset(self.request.POST)
        else:
            ctx['form'] = ProjectForm()
            ctx['formset'] = CrewFormset()
        return ctx


@user_passes_test(lambda u: u.is_contractor(), login_url='/auth/login/contractor')
def project_created_view(request):
    return render(request, 'dashboard/contractor/project-created.html')


# @login_required(login_url='/')
# @permission_required('core.is_manager', login_url='/auth/login/')


@user_passes_test(lambda u: u.is_manager(), login_url='/auth/login/manager')
def manager_home_view(request):
    return render(request, 'dashboard/manager/project-list.html')
    # return HttpResponse(f'{request.user.email} is logged in')


class ManagerProjectListView(UserPassesTestMixin, ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'dashboard/manager/project-list.html'

    # def get_queryset(self):
    #     return Project.objects.filter(creator=self.request.user)

    def test_func(self):
        return self.request.user.is_manager()

    def handle_no_permission(self):
        return redirect_to_login(
            self.request.get_full_path(),
            reverse('login', kwargs={'user_type': 'manager'}),
            'next'
        )


@user_passes_test(lambda u: u.is_contractor(), login_url='/auth/login/contractor')
def contractor_home_view(request):
    return render(request, 'dashboard/contractor/templates/dashboard/project-list.html')
    # return HttpResponse(f'{request.user.email} is logged in')


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'dashboard/project-list.html'

    def get_queryset(self):
        if self.request.user.is_contractor():
            return Project.objects.filter(creator=self.request.user)
        elif self.request.user.is_manager():
            return Project.objects.all()


class ContractorProjectDetailView(DetailView):
    model = Project
    # context_object_name = 'project'
    template_name = 'dashboard/project-detail.html'

    # def test_func(self):
    #     return self.request.user.is_contractor()

    # def handle_no_permission(self):
    #     return redirect_to_login(
    #         self.request.get_full_path(),
    #         reverse('login', kwargs={'user_type': 'contractor'}),
    #         'next'
    #     )

#
# class ContractorProjectListView(UserPassesTestMixin, ListView):
#     model = Project
#     context_object_name = 'projects'
#     template_name = 'dashboard/contractor/project-list.html'
#
#     def get_queryset(self):
#         return Project.objects.filter(creator=self.request.user)
#
#     def test_func(self):
#         return self.request.user.is_contractor()
#
#     def handle_no_permission(self):
#         return redirect_to_login(
#             self.request.get_full_path(),
#             reverse('login', kwargs={'user_type': 'contractor'}),
#             'next'
#         )
#
