# Generated by Django 4.2 on 2023-04-27 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anomaly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anomaly_number', models.IntegerField()),
                ('anomaly_type', models.CharField(choices=[('pothole', 'Pothole'), ('patch', 'Patch'), ('webcrack', 'Webcrack')], max_length=8)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('length', models.DecimalField(decimal_places=2, max_digits=6)),
                ('width', models.DecimalField(decimal_places=2, max_digits=6)),
                ('area', models.DecimalField(decimal_places=2, max_digits=9)),
                ('size', models.CharField(max_length=16)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]
