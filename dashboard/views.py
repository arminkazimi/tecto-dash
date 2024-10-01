from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from dashboard.forms import (
    ProjectForm,
    CrewFormset,
)
from dashboard.models import Project


class CreateProjectView(CreateView):
    template_name = 'dashboard/contractor/project-create.html'
    model = Project
    form_class = ProjectForm  # the parent object's form

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
            project = form.save()
            for crew_form in formset:
                crew = crew_form.save(commit=False)
                crew.project = project
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


# @user_passes_test(lambda u: u.is_contractor(), login_url='/auth/login/contractor')
def project_created_view(request):
    return render(request, 'dashboard/contractor/project-created.html')


# @login_required(login_url='/')
# @permission_required('core.is_manager', login_url='/auth/login/')


@user_passes_test(lambda u: u.is_manager(), login_url='/auth/login/manager')
def manager_home_view(request):
    # return render(request, 'manager_dashboard/project-list.html')
    return HttpResponse(f'{request.user.email} is logged in')


@user_passes_test(lambda u: u.is_contractor(), login_url='/auth/login/contractor')
def contractor_home_view(request):
    return render(request, 'dashboard/contractor/project-list.html')
    # return HttpResponse(f'{request.user.email} is logged in')
#
# def test_create_project_view(request):
#     project_form = ProjectForm(request.POST or None)
#
#     crew_formset = CrewFormset(request.POST or None)
#
#     context = {
#         "form": project_form,
#         "formset": crew_formset
#     }
#     if request.POST and request.FILES:
#         print('project form is valid: ', project_form.is_valid())
#         print('crew form is valid: ', crew_formset.is_valid())
#         print('request image: ', request.FILES)
#     if all([project_form.is_valid(), crew_formset.is_valid()]):
#         project_form.save(commit=False)
#         print('project form: ', project_form.cleaned_data)
#         print('crew form: ', crew_formset.cleaned_data)
#     # return render(request, 'dashboard/contractor/test.html', context)
#     return render(request, 'dashboard/contractor/project-create.html', context)
# FORMS = [
#     ('one', ProjectForm1),
#     ('two', ConstructionZoneForm),
#     ('three', ConstructionDurationForm)
# ]
# TEMPLATES = {
#     'one': 'dashboard/contractor/wizard-step1.html',  # Template for Step 1
#     'two': 'dashboard/contractor/wizard-step2.html',  # Template for Step 2
#     'three': 'dashboard/contractor/wizard-step3.html',  # Template for Step 3
# }
#
#
# class TestWizardView(SessionWizardView):
#     # List of forms in the dashboard/contractor/wizard
#     form_list = FORMS
#     # template_name = 'dashboard/contractor/form-dashboard/contractor/wizard.html'
#     file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'dashboard/test'))
#
#     def get_template_names(self):
#         return [TEMPLATES[self.steps.current]]
#
#     def get_form(self, step=None, data=None, files=None):
#         # Override to handle file uploads
#         return super().get_form(step, data, files)
#
#     def done(self, form_list, **kwargs):
#         # Process the form data after all steps are completed
#         project_data = form_list[0].cleaned_data
#         construction_zone_data = form_list[1].cleaned_data
#         duration_data = form_list[2].cleaned_data
#
#         # Access the uploaded photo
#         photo = construction_zone_data['photo']
#         # You can save the photo or perform other processing
#
#         return render(self.request, 'dashboard/contractor/done.html', {
#             'project_data': project_data,
#             'construction_zone_data': construction_zone_data,
#             'duration_data': duration_data,
#         })
