# Generated by Django 4.1.4 on 2023-01-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0002_remove_contact_user_username_contact_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='username',
            field=models.CharField(default='username', max_length=200, null=True),
        ),
    ]