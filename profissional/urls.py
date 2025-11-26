from django.urls import path
from . import views

app_name = "profissional"

urlpatterns = [
    path("login/", views.login_profissional, name="login"),
    path("dashboard/", views.dashboard_profissional, name="dashboard"),
]