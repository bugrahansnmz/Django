# Generated by Django 4.0.5 on 2022-08-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0002_alter_advert_advert_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='advert_date',
            field=models.DateField(auto_created=True, auto_now_add=True),
        ),
    ]