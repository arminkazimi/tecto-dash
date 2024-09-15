from django.urls import path
from registration.views import CustomLoginView

urlpatterns = [
    path('login/<str:user_type>', CustomLoginView.as_view(), name='login'),
    # path('logedin/', check_user_view, name='check-user'),
]
