# Generated by Django 5.1.4 on 2025-03-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='long_description',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
