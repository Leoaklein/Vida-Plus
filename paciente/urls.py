from django.urls import path
from . import views

app_name = "paciente"

urlpatterns = [
    path("login/", views.login_paciente, name="login"),
    path("dashboard/", views.dashboard_paciente, name="dashboard"),
    path("registrar/", views.registrar_paciente, name="registrar"),
]
