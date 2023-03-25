from django.urls import path

from accounts.views import LoginView, RegisterView, ProfileView, UserChangeView, UserPasswordChangeView

from accounts.views import logout_view

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change', UserChangeView.as_view(), name='change'),
    path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name='password_change')
]
