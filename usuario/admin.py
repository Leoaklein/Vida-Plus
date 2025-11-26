from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Campos que vão aparecer na listagem
    list_display = ('username', 'email', 'telefone', 'tipo', 'cpf', 'data_nascimento', 'is_staff', 'crm')
    list_filter = ('tipo', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'cpf', 'crm')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('email', 'tipo', 'cpf','crm', 'data_nascimento')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username', 'email', 'tipo', 'telefone','crm','cpf', 'data_nascimento', 'password1', 'password2', 'is_staff', 'is_superuser',
            'is_active'),
        }),
    )