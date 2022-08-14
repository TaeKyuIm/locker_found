from django.urls import path
from .views import CustomUserCreate, LoginAPIView, LogoutAPIView

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    # path('userList/',UserList.as_view()),
]