# Generated by Django 4.2.5 on 2023-11-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_alter_data_d_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='d_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
