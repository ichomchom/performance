# Generated by Django 2.2.2 on 2019-06-20 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adr', '0004_auto_20190619_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='closed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='date_inquiry',
            field=models.DateField(blank=True, null=True),
        ),
    ]