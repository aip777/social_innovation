# Generated by Django 3.1.2 on 2020-11-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcms', '0010_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='community_about',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
