# Generated by Django 4.2.3 on 2023-08-19 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Firstapp', '0003_inputs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputs',
            name='firstname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='inputs',
            name='lastname',
            field=models.CharField(max_length=200),
        ),
    ]
