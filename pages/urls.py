from django.urls import path
from . import views

urlpatterns = [
    path('', views.switch_panel_view)
]
