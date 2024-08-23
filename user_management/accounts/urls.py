from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, AdminUserListView, AdminUserDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('admin/users/', AdminUserListView.as_view(), name='admin-user-list'),
    path('admin/users/<int:id>/', AdminUserDeleteView.as_view(), name='admin-user-delete'),

]
