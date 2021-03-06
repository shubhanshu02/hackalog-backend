from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()
class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Fields', {'fields': ('uid', 'name', 'college', 'github_handle', 'bio', 'interests','photoURL')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('uid', 'username', 'password1', 'password2'),
        }),
    )
    list_display = ('uid', 'username', 'github_handle', 'name', 'email', 'is_staff')
    search_fields = ('username', 'github_handle', 'name', 'email','photoURL')
admin.site.register(User, MyUserAdmin)