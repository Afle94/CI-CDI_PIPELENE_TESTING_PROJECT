from django.contrib import admin
from cd_cdi_Automation.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'date_joined')
    search_fields = ('name', 'email', 'position')
    list_filter = ('position', 'date_joined')

admin.site.register(Employee, EmployeeAdmin)
