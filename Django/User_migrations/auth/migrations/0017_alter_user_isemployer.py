# Generated by Django 4.0.5 on 2022-08-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0016_alter_user_isemployer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isEmployer',
            field=models.BooleanField(blank=True, default=False, verbose_name='isEmployer'),
        ),
    ]
