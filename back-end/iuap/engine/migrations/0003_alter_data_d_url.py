# Generated by Django 4.2.5 on 2023-11-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_data_queue_delete_uploadedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='d_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]
