# Generated by Django 5.1.6 on 2025-02-23 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='shart_size',
            field=models.CharField(default='zero', max_length=1),
            preserve_default=False,
        ),
    ]
