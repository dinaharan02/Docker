# Generated by Django 4.2 on 2023-04-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mobile_number',
            field=models.IntegerField(default=0),
        ),
    ]