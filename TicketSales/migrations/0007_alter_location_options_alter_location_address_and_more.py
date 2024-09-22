# Generated by Django 5.1.1 on 2024-09-21 20:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TicketSales", "0006_alter_concert_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="location",
            options={"verbose_name": "مکان", "verbose_name_plural": "مکان"},
        ),
        migrations.AlterField(
            model_name="location",
            name="address",
            field=models.CharField(
                default="Iran-Tehran",
                help_text="آدرس کامل محل را وارد کنید",
                max_length=500,
                verbose_name="آدرس",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="capacity",
            field=models.IntegerField(
                help_text="حداکثر ظرفیت محل",
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="ظرفیت",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="closing_time",
            field=models.TimeField(blank=True, null=True, verbose_name="زمان بسته شدن"),
        ),
        migrations.AlterField(
            model_name="location",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده در"),
        ),
        migrations.AlterField(
            model_name="location",
            name="id_number",
            field=models.IntegerField(
                primary_key=True, serialize=False, verbose_name="شماره شناسه"
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="فعال است"),
        ),
        migrations.AlterField(
            model_name="location",
            name="latitude",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                max_digits=9,
                null=True,
                verbose_name="عرض جغرافیایی",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="location_type",
            field=models.CharField(
                choices=[
                    ("restaurant", "رستوران"),
                    ("shop", "خرید کنید"),
                    ("service_center", "مرکز خدمات"),
                    ("concert", "کنسرت"),
                ],
                max_length=50,
                verbose_name="نوع مکان",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="longitude",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                max_digits=9,
                null=True,
                verbose_name="طول جغرافیایی",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="name",
            field=models.CharField(
                help_text="نام مکان را وارد کنید",
                max_length=100,
                verbose_name="نام مکان",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="opening_time",
            field=models.TimeField(blank=True, null=True, verbose_name="زمان افتتاحیه"),
        ),
        migrations.AlterField(
            model_name="location",
            name="phone",
            field=models.CharField(
                help_text="یک شماره تلفن معتبر وارد کنید",
                max_length=11,
                null=True,
                verbose_name="شماره تلفن",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="به روز شده در"),
        ),
        migrations.AlterField(
            model_name="location",
            name="website",
            field=models.URLField(blank=True, null=True, verbose_name="وب سایت"),
        ),
    ]
