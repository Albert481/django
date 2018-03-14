# Generated by Django 2.0.3 on 2018-03-14 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180314_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(default='null', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ethaddress',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
