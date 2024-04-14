# Generated by Django 5.0.4 on 2024-04-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0005_rename_clothes_cloth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='clothes_photos/')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('color', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cloth',
        ),
    ]
