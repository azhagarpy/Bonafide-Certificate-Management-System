# Generated by Django 4.2.9 on 2024-03-08 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='rejectReson',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
