# Generated by Django 5.1.1 on 2024-09-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "TicketSales",
            "0008_alter_timeslot_options_alter_timeslot_end_date_time_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="timeslot",
            name="end_date_time",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="تاریخ و زمان پایان"
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="start_date_time",
            field=models.DateTimeField(verbose_name="تاریخ و زمان شروع"),
        ),
    ]
