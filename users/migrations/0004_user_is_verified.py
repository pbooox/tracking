# Generated by Django 2.2.9 on 2020-02-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200217_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=True, help_text='Set to true when the user have verified its email address.', verbose_name='verified'),
        ),
    ]