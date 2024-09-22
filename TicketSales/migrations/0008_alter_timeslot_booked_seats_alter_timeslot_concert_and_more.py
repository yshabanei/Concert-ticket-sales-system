# Generated by Django 5.1.1 on 2024-09-22 04:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TicketSales", "0007_alter_location_options_alter_location_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timeslot",
            name="booked_seats",
            field=models.IntegerField(
                default=0,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="صندلی های رزرو شده",
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="concert",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="TicketSales.concert",
                verbose_name="کنسرت",
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده در"),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="end_date_time",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="تاریخ و زمان پایان"
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="فعال است"),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="TicketSales.location",
                verbose_name="مکان",
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="price_per_seat",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="قیمت هر صندلی",
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="remarks",
            field=models.TextField(blank=True, null=True, verbose_name="نکات تکمیلی"),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="seats",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="تعداد صندلی",
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="start_date_time",
            field=models.DateTimeField(verbose_name="تاریخ و زمان شروع"),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="status",
            field=models.CharField(
                choices=[
                    ("Start", "شروع کنید"),
                    ("End", "پایان"),
                    ("Sales", "فروش"),
                    ("active", "فعال"),
                    ("cancelled", "لغو شد"),
                    ("completed", "تکمیل شد"),
                ],
                default="active",
                max_length=10,
                verbose_name="وضعیت",
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="به روز شده در"),
        ),
    ]
