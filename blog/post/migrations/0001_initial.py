# Generated by Django 5.0 on 2023-12-06 23:12

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('texto', models.TextField()),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('puntaje', models.IntegerField(default=5)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.autor')),
            ],
        ),
    ]
