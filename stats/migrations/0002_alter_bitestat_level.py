# Generated by Django 4.0.5 on 2022-06-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitestat',
            name='level',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
