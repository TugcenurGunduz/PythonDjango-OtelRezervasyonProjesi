# Generated by Django 3.0.4 on 2020-06-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_auto_20200603_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationroom',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Canceled', 'Canceled'), ('New', 'New')], default='New', max_length=10),
        ),
    ]
