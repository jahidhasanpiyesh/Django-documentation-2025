# Generated by Django 5.1.6 on 2025-02-25 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_verbose_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='normal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='verbose',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name="person's first name"),
        ),
    ]
