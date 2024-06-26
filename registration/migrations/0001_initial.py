# Generated by Django 5.0.4 on 2024-04-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('field', models.CharField(max_length=100)),
            ],
        ),
    ]
