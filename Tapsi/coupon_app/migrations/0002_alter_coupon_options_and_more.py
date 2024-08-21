# Generated by Django 5.1 on 2024-08-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'Coupon', 'verbose_name_plural': 'Coupons'},
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_availability',
            field=models.BooleanField(help_text='Indicate if the coupon is currently available for use.', verbose_name='Coupon Availability'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='expire_date',
            field=models.DateField(help_text='Enter the expiration date of the coupon.', verbose_name='Expiration Date'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='percent',
            field=models.FloatField(help_text='Enter the discount percentage provided by the coupon.', verbose_name='Discount Percentage'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='title',
            field=models.CharField(help_text='Enter the title of the coupon.', max_length=50, verbose_name='Coupon Title'),
        ),
    ]
