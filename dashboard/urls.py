from django.urls import path

from dashboard.views import (
    manager_home_view,
    contractor_home_view,
    # test_formset_view,
    # CreateProjectWizardView,
    # TestWizardView,
    # test_create_project_view,
    CreateProjectView,
    project_created_view,
    ProjectListView,
    ContractorProjectDetailView,
)

urlpatterns = [
    # path('home/', homeView.as_view(), name='manager-home'),
    path('manager/home/', manager_home_view, name='manager-home'),
    path('contractor/home/', ProjectListView.as_view(), name='contractor-home'),
    path('create-project/', CreateProjectView.as_view(), name='create-project'),
    path('contractor/projects/', ProjectListView.as_view(), name='project-list'),
    path('contractor/projects/<pk>', ContractorProjectDetailView.as_view(), name='project-detail'),
    path('contractor/project-created/', project_created_view, name='project-created'),
    # path('create-project/', test_formset_view, name='create-project'),
    # path('test/', test_formset_view, name='test'),
    # path('wizard/', CreateProjectWizardView.as_view(), name='form-wizard'),
    # path('test-wizard/', TestWizardView.as_view(), name='test-wizard'),
    # path('test/', CreateProjectView.as_view(), name='test'),
]
