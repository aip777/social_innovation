# Generated by Django 3.1.2 on 2020-11-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcms', '0003_auto_20201103_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_details_one',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_details_two',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
