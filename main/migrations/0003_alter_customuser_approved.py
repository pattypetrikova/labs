# Generated by Django 4.2 on 2023-09-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customuser_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
