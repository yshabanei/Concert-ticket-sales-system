# Generated by Django 5.1.1 on 2024-09-27 09:39

import django_jalali.db.models
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TicketSales", "0010_alter_timeslot_end_date_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timeslot",
            name="end_date_time",
            field=django_jalali.db.models.jDateTimeField(
                blank=True, null=True, verbose_name="تاریخ و زمان پایان"
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="price_per_seat",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=8,
                null=True,
                verbose_name="قیمت هر صندلی",
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="start_date_time",
            field=django_jalali.db.models.jDateTimeField(
                verbose_name="تاریخ و زمان شروع"
            ),
        ),
        migrations.AddIndex(
            model_name="timeslot",
            index=models.Index(
                fields=["start_date_time"], name="TicketSales_start_d_2f1a88_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="timeslot",
            index=models.Index(fields=["status"], name="TicketSales_status_a4176a_idx"),
        ),
    ]
