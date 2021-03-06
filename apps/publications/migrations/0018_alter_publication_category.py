# Generated by Django 3.2.4 on 2021-06-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0017_alter_publication_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('GL', 'General'), ('Closures', 'CS'), ('VS', 'Vacancies'), ('CN', 'Consultations'), ('JS', 'Judicial Sales'), ('NR', 'Newsletters'), ('Tenders', 'Tenders')], default='GL', max_length=50),
        ),
    ]
