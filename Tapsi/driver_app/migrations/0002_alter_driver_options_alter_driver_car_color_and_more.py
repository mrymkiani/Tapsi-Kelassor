# Generated by Django 5.1 on 2024-08-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'Driver', 'verbose_name_plural': 'Drivers'},
        ),
        migrations.AlterField(
            model_name='driver',
            name='car_color',
            field=models.CharField(help_text="Enter the color of the driver's car.", max_length=50, verbose_name='Car Color'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='car_model',
            field=models.CharField(help_text="Enter the model of the driver's car.", max_length=50, verbose_name='Car Model'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='car_plate',
            field=models.CharField(help_text="Enter the plate number of the driver's car.", max_length=50, verbose_name='Car Plate Number'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(help_text='Enter the first name of the driver.', max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(help_text='Enter the last name of the driver.', max_length=50, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='phone_number',
            field=models.CharField(help_text='Enter the phone number of the driver.', max_length=11, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='wallet',
            field=models.FloatField(help_text="Enter the current balance in the driver's wallet.", verbose_name='Wallet Balance'),
        ),
    ]
