# Generated by Django 3.2.19 on 2024-05-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
