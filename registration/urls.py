from django.urls import path
from registration.views import CustomLoginView, check_user_view

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logedin/', check_user_view, name='check-user'),
]
