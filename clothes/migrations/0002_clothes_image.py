# Generated by Django 5.0.4 on 2024-04-14 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='clothes_photos/'),
        ),
    ]