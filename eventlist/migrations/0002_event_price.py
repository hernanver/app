# Generated by Django 4.0.2 on 2022-12-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
