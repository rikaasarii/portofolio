# Generated by Django 3.2.15 on 2023-03-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='images'),
        ),
    ]
