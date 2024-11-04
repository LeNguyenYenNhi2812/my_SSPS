# Generated by Django 5.1.2 on 2024-11-04 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('printer', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='print_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'success'), ('2', 'failed'), ('3', 'pending')], max_length=7)),
                ('file_to_be_printed', models.FileField(upload_to='files/')),
                ('orientation', models.CharField(choices=[('portrait', 'portrait'), ('landscape', 'landscape')], default='portrait', max_length=10)),
                ('sided', models.CharField(choices=[('single', 'single'), ('double', 'double')], default='single', max_length=6)),
                ('page_side', models.CharField(choices=[('A3', 'A3'), ('A4', 'A4')], default='A4', max_length=2)),
                ('copies', models.IntegerField(default=1)),
                ('timer_start', models.DateTimeField(auto_now_add=True)),
                ('timer_end', models.DateTimeField()),
                ('page_cost', models.IntegerField(default=0)),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printer.printer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
