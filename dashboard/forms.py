# forms.py
from django import forms
from django.forms import modelformset_factory, formset_factory

from dashboard.models import Project, Crew


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'level',
            'start_date',
            'end_date',
        ]


class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = [
            'title',
            'crew_count',
            'start_time',
            'end_time'
        ]


CrewFormset = formset_factory(
    CrewForm,
    extra=1
)


# Step 1: Project Name and Geographical Level
# class ProjectForm1(forms.Form):
#     project_name = forms.CharField(label="Project Name", max_length=100)
#     geographical_level = forms.ChoiceField(
#         label="Geographical Level",
#         choices=[('level1', 'Level 1'), ('level2', 'Level 2'), ('level3', 'Level 3'), ('level4', 'Level 4')],
#         widget=forms.RadioSelect
#     )


# Step 2: Construction Zone with Image Upload
# class ConstructionZoneForm(forms.Form):
#     # construction_zone = forms.CharField(widget=forms.HiddenInput())
#     photo = forms.ImageField(label="Upload Construction Zone Photo", required=True)  # Field for photo upload
#

# Step 3: Construction Duration and Crew Name
# class ConstructionDurationForm(forms.Form):
#     start_date = forms.DateField(widget=forms.SelectDateWidget)
#     end_date = forms.DateField(widget=forms.SelectDateWidget)
#     crew_name_day = forms.CharField(label="Day Crew Name", max_length=100)
#     day_workers = forms.IntegerField(label="Number of Day Workers")
#     day_start_time = forms.TimeField(label="Day Shift Start")
#     day_end_time = forms.TimeField(label="Day Shift End")
#
#     crew_name_night = forms.CharField(label="Night Crew Name", max_length=100)
#     night_workers = forms.IntegerField(label="Number of Night Workers")
#     night_start_time = forms.TimeField(label="Night Shift Start")
#     night_end_time = forms.TimeField(label="Night Shift End")
