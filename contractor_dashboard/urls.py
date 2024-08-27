from django.urls import path
from contractor_dashboard.views import homeView

urlpatterns = [
    path('home/', homeView, name='contractor-home'),
]
