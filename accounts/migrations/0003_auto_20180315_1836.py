# Generated by Django 2.0.3 on 2018-03-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180315_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth_user',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
