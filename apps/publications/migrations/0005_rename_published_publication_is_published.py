# Generated by Django 3.2.4 on 2021-06-12 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_publication_is_deleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='published',
            new_name='is_published',
        ),
    ]
