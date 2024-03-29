# Generated by Django 3.1.2 on 2020-11-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcms', '0009_remove_navbar_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(blank=True, max_length=100)),
                ('community_about', models.CharField(blank=True, max_length=2000)),
                ('community_facebook', models.CharField(blank=True, max_length=500)),
                ('community_twitter', models.CharField(blank=True, max_length=500)),
                ('community_linkedin', models.CharField(blank=True, max_length=500)),
                ('community_instagram', models.CharField(blank=True, max_length=500)),
                ('nav_title', models.CharField(blank=True, max_length=100)),
                ('nav_link_one', models.CharField(blank=True, max_length=50)),
                ('nav_link_two', models.CharField(blank=True, max_length=50)),
                ('nav_link_three', models.CharField(blank=True, max_length=50)),
                ('nav_link_four', models.CharField(blank=True, max_length=50)),
                ('nav_link_five', models.CharField(blank=True, max_length=50)),
                ('nav_link_six', models.CharField(blank=True, max_length=50)),
                ('nav_link_seven', models.CharField(blank=True, max_length=50)),
                ('contact_title', models.CharField(blank=True, max_length=250)),
                ('contact_address', models.CharField(blank=True, max_length=500)),
                ('contact_phone', models.CharField(blank=True, max_length=250)),
                ('contact_email', models.CharField(blank=True, max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Footer',
                'verbose_name_plural': 'Footer',
            },
        ),
    ]
