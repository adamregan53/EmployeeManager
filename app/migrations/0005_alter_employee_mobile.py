# Generated by Django 4.1.7 on 2023-03-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_employee_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(max_length=50),
        ),
    ]