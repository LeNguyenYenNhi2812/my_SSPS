# Generated by Django 5.1.2 on 2024-11-23 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('total_amount', models.FloatField(blank=True, default=0, null=True)),
            ],
        ),
    ]
