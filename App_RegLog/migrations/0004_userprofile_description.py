# Generated by Django 4.0.5 on 2022-06-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_RegLog', '0003_userprofile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
