# Generated by Django 3.1.2 on 2020-10-31 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='company_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
