# Generated by Django 5.0 on 2024-02-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='phonenumber',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='register',
            name='phonenumber',
            field=models.CharField(max_length=100),
        ),
    ]
