# Generated by Django 3.0.4 on 2020-06-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20200602_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationroom',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Canceled', 'Canceled'), ('Accepted', 'Accepted')], default='New', max_length=10),
        ),
    ]
