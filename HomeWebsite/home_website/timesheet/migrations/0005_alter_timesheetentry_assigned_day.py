# Generated by Django 4.1 on 2023-08-09 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timesheet", "0004_timesheetentry_day_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timesheetentry",
            name="assigned_day",
            field=models.CharField(
                choices=[
                    ("Monday", "Monday"),
                    ("Tuesday", "Tuesday"),
                    ("Wednesday", "Wednesday"),
                    ("Thursday", "Thursday"),
                    ("Friday", "Friday"),
                    ("Saturday", "Saturday"),
                    ("Sunday", "Sunday"),
                ],
                default="Monday",
                max_length=10,
            ),
        ),
    ]
