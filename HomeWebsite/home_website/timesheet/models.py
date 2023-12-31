from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username


class TimesheetEntry(models.Model):
    class Weekday(models.TextChoices):
        mon = "Monday", "Monday"
        tue = "Tuesday", "Tuesday"
        wed = "Wednesday", "Wednesday"
        thu = "Thursday", "Thursday"
        fri = "Friday", "Friday"
        sat = 'Saturday', 'Saturday'
        sun = "Sunday", "Sunday"
        
    class Times(models.TextChoices):
        morn = 'Morning', 'Morning'
        aft = 'Afternoon', 'Afternoon'
        even = 'Evening', 'Evening'
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    activity = models.TextField(max_length=1000)
    assigned_day = models.CharField(max_length=10, choices=Weekday.choices, default='Monday')
    day_time = models.CharField(max_length=10, choices=Times.choices, default='Morning')
    
    
class loan_personal_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)
    date_of_birth = models.DateField()
    home_number = PhoneNumberField(null=True, blank=True,)
    mobile_number = PhoneNumberField(null=True, blank=True)
    amount = models.IntegerField(default=1)
    repayment = models.DateField()
    amount_due = models.IntegerField()
