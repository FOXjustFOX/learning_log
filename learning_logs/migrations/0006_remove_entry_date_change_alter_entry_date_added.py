# Generated by Django 4.1.5 on 2023-01-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_entry_date_change'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='date_change',
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
