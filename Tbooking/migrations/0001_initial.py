# Generated by Django 3.0.2 on 2020-03-31 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('Cid', models.AutoField(primary_key=True, serialize=False)),
                ('CityName', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
                ('Special_Offer', models.BooleanField(default=False)),
                ('Citypic', models.ImageField(null=True, upload_to='pics')),
                ('Depart_date', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('CityName', models.CharField(max_length=100)),
                ('Total', models.CharField(max_length=100)),
                ('Booking', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
