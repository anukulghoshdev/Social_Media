# Generated by Django 4.0.5 on 2022-06-12 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='captioin',
            new_name='caption',
        ),
    ]