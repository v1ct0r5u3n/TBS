from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager

# Register your models here.
from .models import Address,Employee,Customer,Person

admin.site.register(Address)
#admin.site.register(Employee)
#admin.site.register(Customer)
#admin.site.register(Person)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	search_fields = ['name','alias','mobile']
	list_display = ('__str__','mobile','balance','due','personal_manager')
	list_display_links = ('__str__','mobile')

#@admin.register(Employee)
#class EmployeeAdmin(admin.ModelAdmin):
#	pass
#admin.site.register(Employee,BaseUserManager)

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import Employee


class EmployeeCreationForm(forms.ModelForm):
    """A form for creating new employees. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ('name', 'mobile')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("两次输入的密码不一致")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        employee = super().save(commit=False)
        employee.set_password(self.cleaned_data["password1"])
        if commit:
            employee.save()
        return employee


class EmployeeChangeForm(forms.ModelForm):
    """A form for updating employees. Includes all the fields on
    the employee, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Employee
        fields = ('name','alias','mobile','id_card_no','id_address','is_active', 'is_admin')


class EmployeeAdmin(BaseUserAdmin):
    # The forms to add and change employee instances
    form = EmployeeChangeForm
    add_form = EmployeeCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name','alias','mobile','is_active','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('name','alias','mobile','id_card_no','id_address')}),
        ('状态', {'fields': ('is_active','is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','alias','mobile','id_card_no','id_address','password1', 'password2'),
        }),
    )
    search_fields = ('name','alias','mobile')
    ordering = ('mobile',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(Employee, EmployeeAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)