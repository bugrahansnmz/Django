# Generated by Django 4.0.5 on 2022-08-21 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isEmployer',
            field=models.BooleanField(default=False),
        ),
    ]