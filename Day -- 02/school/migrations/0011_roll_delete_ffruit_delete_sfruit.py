# Generated by Django 5.1.6 on 2025-02-23 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_ffruit_sfruit_delete_fruit'),
    ]

    operations = [
        migrations.CreateModel(
            name='roll',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='fFruit',
        ),
        migrations.DeleteModel(
            name='sFruit',
        ),
    ]
