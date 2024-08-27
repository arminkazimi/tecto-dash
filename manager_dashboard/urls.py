from django.urls import path
from manager_dashboard.views import homeView

urlpatterns = [
    # path('home/', homeView.as_view(), name='manager-home'),
    path('home/', homeView, name='manager-home'),
]
