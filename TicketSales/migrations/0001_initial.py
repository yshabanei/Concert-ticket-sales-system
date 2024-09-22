# Generated by Django 5.1.1 on 2024-09-21 19:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Concert",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Concert Name")),
                (
                    "singer_name",
                    models.CharField(max_length=100, verbose_name="Singer Name"),
                ),
                (
                    "length",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Concert Length (minutes)",
                    ),
                ),
                (
                    "Concert_picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Concert_pictures/",
                        verbose_name="عکس پروفایل",
                    ),
                ),
                ("date", models.DateTimeField(verbose_name="Concert Date and Time")),
                (
                    "location",
                    models.CharField(max_length=255, verbose_name="Concert Location"),
                ),
                (
                    "available_tickets",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Available Tickets",
                    ),
                ),
                (
                    "ticket_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Ticket Price"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Concert Description"
                    ),
                ),
                (
                    "ticket_status",
                    models.CharField(
                        choices=[
                            ("available", "Available"),
                            ("sold_out", "Sold Out"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="available",
                        max_length=10,
                        verbose_name="Ticket Status",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id_number", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(
                        help_text="Enter the name of the location",
                        max_length=100,
                        verbose_name="Location Name",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        default="Iran-Tehran",
                        help_text="Enter the full address of the location",
                        max_length=500,
                        verbose_name="Address",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="Enter a valid phone number",
                        max_length=11,
                        null=True,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "capacity",
                    models.IntegerField(
                        help_text="Maximum capacity of the location",
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Capacity",
                    ),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True,
                        decimal_places=6,
                        max_digits=9,
                        null=True,
                        verbose_name="Latitude",
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True,
                        decimal_places=6,
                        max_digits=9,
                        null=True,
                        verbose_name="Longitude",
                    ),
                ),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="Website"),
                ),
                (
                    "opening_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="Opening Time"
                    ),
                ),
                (
                    "closing_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="Closing Time"
                    ),
                ),
                (
                    "location_type",
                    models.CharField(
                        choices=[
                            ("restaurant", "Restaurant"),
                            ("shop", "Shop"),
                            ("service_center", "Service Center"),
                        ],
                        max_length=50,
                        verbose_name="Location Type",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="نام")),
                (
                    "family",
                    models.CharField(max_length=100, verbose_name="نام خانوادگی"),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("Man", "مرد"), ("Woman", "زن")],
                        max_length=6,
                        verbose_name="جنسیت",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(blank=True, null=True, verbose_name="تاریخ تولد"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="آدرس ایمیل"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="شماره تلفن"
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_pictures/",
                        verbose_name="عکس پروفایل",
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True, max_length=255, verbose_name="بیوگرافی"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="آدرس"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="تاریخ ثبت\u200c نام"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="تاریخ آخرین بروزرسانی"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TimeSlot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "start_date_time",
                    models.DateTimeField(verbose_name="Start Date and Time"),
                ),
                (
                    "end_date_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="End Date and Time"
                    ),
                ),
                (
                    "seats",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Number of Seats",
                    ),
                ),
                (
                    "price_per_seat",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=8,
                        null=True,
                        verbose_name="Price per Seat",
                    ),
                ),
                (
                    "booked_seats",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Booked Seats",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Start", "Start"),
                            ("End", "End"),
                            ("Sales", "Sales"),
                            ("active", "Active"),
                            ("cancelled", "Cancelled"),
                            ("completed", "Completed"),
                        ],
                        default="active",
                        max_length=10,
                        verbose_name="Status",
                    ),
                ),
                (
                    "remarks",
                    models.TextField(
                        blank=True, null=True, verbose_name="Additional Remarks"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "concert",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="TicketSales.concert",
                        verbose_name="Concert",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="TicketSales.location",
                        verbose_name="Location",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=1000)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Ticket Price",
                    ),
                ),
                (
                    "Ticket_picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Ticket_pictures/",
                        verbose_name="عکس پروفایل",
                    ),
                ),
                (
                    "purchase_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ خرید"),
                ),
                (
                    "ticket_code",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="کد بلیط"
                    ),
                ),
                (
                    "ticket_status",
                    models.CharField(
                        choices=[
                            ("active", "فعال"),
                            ("expired", "منقضی"),
                            ("canceled", "لغو شده"),
                        ],
                        default="active",
                        max_length=10,
                        verbose_name="وضعیت بلیط",
                    ),
                ),
                (
                    "reserved_seats",
                    models.IntegerField(
                        default=1, verbose_name="تعداد صندلی\u200cهای رزرو شده"
                    ),
                ),
                (
                    "expiration_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="تاریخ انقضا"
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("credit_card", "کارت اعتباری"),
                            ("paypal", "PayPal"),
                            ("cash", "نقدی"),
                        ],
                        max_length=20,
                        verbose_name="نحوه پرداخت",
                    ),
                ),
                (
                    "additional_notes",
                    models.TextField(
                        blank=True, null=True, verbose_name="توضیحات اضافی"
                    ),
                ),
                (
                    "profilemodel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tickets",
                        to="TicketSales.profile",
                        verbose_name="Profile",
                    ),
                ),
                (
                    "timemodel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tickets",
                        to="TicketSales.timeslot",
                        verbose_name="TimeSlot",
                    ),
                ),
            ],
        ),
    ]
