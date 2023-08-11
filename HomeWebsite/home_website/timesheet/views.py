
from django.shortcuts import render, redirect
from .models import TimesheetEntry, loan_personal_info
from django.contrib.auth.decorators import login_required

from timesheet.forms import TimesheetEntryForm, loan_personal_info_form
from .models import TimesheetEntry, loan_personal_info


@login_required
def submit_timesheet(request):
    user_name = request.user
    
    if request.method == 'POST':
        form = TimesheetEntryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = TimesheetEntryForm()
        
    entries = TimesheetEntry.objects.filter(user=request.user)
    
    context = {
        'entries': entries,
        'form':form,
        'user_name':user_name
    }
    
    return render(request, 'timesheet/index.html', context)
    

'''
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

    return render(request, 'chore_site\loan_application.html', {'user_name':user_name,
                                                                'loans':loans,
                                                                'loan_application_form':loan_application_form,
                                                                })
    '''