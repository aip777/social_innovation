# Generated by Django 3.1.2 on 2020-11-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcms', '0017_auto_20201117_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='icon_reference',
            field=models.CharField(choices=[('mh-id-1', '1'), ('mh-id-2', '2'), ('mh-id-3', '3'), ('mh-id-4', '4')], default=1, max_length=500),
            preserve_default=False,
        ),
    ]
