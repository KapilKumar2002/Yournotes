# Generated by Django 4.1 on 2022-10-18 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobilenumber',
            field=models.CharField(max_length=10),
        ),
    ]
