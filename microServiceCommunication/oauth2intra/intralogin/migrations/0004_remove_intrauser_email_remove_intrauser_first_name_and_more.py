# Generated by Django 5.0 on 2024-02-06 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intralogin', '0003_remove_intrauser_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intrauser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='intrauser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='intrauser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='intrauser',
            name='login',
        ),
    ]
