# Generated by Django 5.1.2 on 2024-11-02 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_delete_searchlog_spso_image_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchase_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('status', models.CharField(choices=[('unpaid', 'Unpaid'), ('paid', 'Paid')], default='unpaid', max_length=10)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_orders', to='user.student')),
            ],
        ),
    ]
