# Generated by Django 2.2.2 on 2019-06-20 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='date_inquiry',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]