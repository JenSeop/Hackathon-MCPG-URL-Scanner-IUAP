# Generated by Django 4.2.5 on 2023-11-13 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('d_date', models.DateTimeField(auto_now_add=True)),
                ('d_data', models.JSONField(default=dict)),
                ('d_status', models.CharField(default='false', max_length=10)),
                ('d_url', models.FileField(upload_to='apk/')),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('q_id', models.AutoField(primary_key=True, serialize=False)),
                ('q_try', models.IntegerField(default=0)),
                ('d_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.data')),
            ],
        ),
        migrations.DeleteModel(
            name='UploadedFile',
        ),
    ]
