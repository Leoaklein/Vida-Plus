from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = "profissional"

urlpatterns = [
    path("login/", views.login_profissional, name="login"),
    path('logout/', LogoutView.as_view(next_page='profissional:login'), name='logout'),
    path("dashboard/", views.dashboard_profissional, name="dashboard"),
]