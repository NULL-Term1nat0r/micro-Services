# Generated by Django 5.0 on 2024-02-06 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intralogin', '0002_alter_intrauser_managers_alter_intrauser_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intrauser',
            name='image_url',
        ),
    ]
