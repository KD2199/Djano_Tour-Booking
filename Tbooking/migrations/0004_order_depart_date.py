# Generated by Django 3.0.2 on 2020-03-31 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tbooking', '0003_auto_20200331_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Depart_date',
            field=models.CharField(default='', max_length=100),
        ),
    ]
