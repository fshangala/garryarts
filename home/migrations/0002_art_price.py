# Generated by Django 4.1.4 on 2022-12-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
