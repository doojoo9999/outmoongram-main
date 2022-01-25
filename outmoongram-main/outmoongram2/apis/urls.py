from django.urls import path
from apis.v1 import UserCreateView, UserLoginView, UserLogoutView

urlpatterns = [
    path('v1/users/create/', UserCreateView.as_view(), name='apis_v1_create'),
    path('v1/users/login/', UserLoginView.as_view(), name='apis_v1_login'),
    path('v1/user/logout/', UserLogoutView.as_view(), name='apis_v1_logout'),
]

