# Generated by Django 4.2 on 2023-04-14 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_userprofile_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'User Profile'},
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='User Profile',
        ),
    ]