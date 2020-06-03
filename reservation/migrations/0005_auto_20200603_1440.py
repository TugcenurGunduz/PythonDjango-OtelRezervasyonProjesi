# Generated by Django 3.0.4 on 2020-06-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_auto_20200603_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationroom',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('New', 'New'), ('Canceled', 'Canceled')], default='New', max_length=10),
        ),
    ]
