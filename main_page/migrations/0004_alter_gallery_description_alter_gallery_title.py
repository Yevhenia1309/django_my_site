# Generated by Django 4.1.5 on 2023-02-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_rename_title_reservation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]