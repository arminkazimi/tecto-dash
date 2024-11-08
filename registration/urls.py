from django.contrib.auth.views import LogoutView
from django.urls import path

from registration.views import CustomLoginView

urlpatterns = [
    path('login/<str:user_type>', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
