# Generated by Django 3.0.2 on 2020-03-31 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tbooking', '0002_auto_20200331_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='Cid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
