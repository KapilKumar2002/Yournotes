# Generated by Django 4.1 on 2022-10-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_contact_mobilenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobilenumber',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]
