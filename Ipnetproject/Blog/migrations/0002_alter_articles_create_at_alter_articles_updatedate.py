# Generated by Django 4.2.1 on 2023-05-30 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='create_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='updateDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
