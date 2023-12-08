# Generated by Django 3.0 on 2023-09-21 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0038_profile_sgen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addbook',
            name='addate',
        ),
        migrations.RemoveField(
            model_name='addbook',
            name='is_avail',
        ),
        migrations.RemoveField(
            model_name='addbook',
            name='isbn',
        ),
        migrations.AddField(
            model_name='addbook',
            name='add_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addbook',
            name='bstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addbook',
            name='ncopies',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
