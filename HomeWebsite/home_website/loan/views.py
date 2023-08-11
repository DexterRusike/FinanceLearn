from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from timesheet.forms import TimesheetEntryForm, loan_personal_info_form
from timesheet.models import loan_personal_info

# Create your views here.
def loan_application(request):
    user_name = request.user
    
    if request.method == 'POST':
        loan_application_form = loan_personal_info_form(request.POST)
        if loan_application_form.is_valid():
            instance = loan_application_form.save(commit=False)
            instance.user = request.user
            instance.save()
            
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        loan_application_form = loan_personal_info_form()
    
    loans = loan_personal_info.objects.filter(user=request.user)

    return render(request, 'loan\index.html', {'user_name':user_name,
                                                                'loans':loans,
                                                                'loan_application_form':loan_application_form,
                                                                })