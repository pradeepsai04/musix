# Generated by Django 4.0.2 on 2023-04-20 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='video',
            field=models.FileField(default='NULL', upload_to='videos/'),
        ),
    ]
