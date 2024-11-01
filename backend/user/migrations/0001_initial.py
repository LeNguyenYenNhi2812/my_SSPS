# Generated by Django 5.1.2 on 2024-11-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=20)),
                ('day_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('lastSignedIn', models.DateTimeField(auto_now_add=True)),
                ('allowed_rule', models.CharField(default='customer', max_length=20)),
            ],
        ),
    ]
