# Generated by Django 3.2.6 on 2021-10-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20211019_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='first_last',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]