# Generated by Django 5.1.6 on 2025-02-23 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_person_shart_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='shart_color',
            field=models.CharField(choices=[('B', 'Black'), ('R', 'Red'), ('W', 'White')], max_length=3),
        ),
    ]
