from django.contrib import admin
from adminapplication.models import EmployeeDetails

# Register your models here.
class EmployeeDetailsAdmin(admin.ModelAdmin):
	'''
		Admin View for EmployeeDetails
	'''
	list_display=('empid', 'empname', 'empdesignation', 'empdeparment', 'empage', 'empbloodgroup', 'empemailid')

admin.site.register(EmployeeDetails, EmployeeDetailsAdmin)
# admin.site.register(Model Class Name, Admin Class Name)