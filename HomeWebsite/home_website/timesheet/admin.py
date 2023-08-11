from django.contrib import admin
from .models import TimesheetEntry, loan_personal_info

# Register your models here.
admin.site.register(TimesheetEntry)
admin.site.register(loan_personal_info)