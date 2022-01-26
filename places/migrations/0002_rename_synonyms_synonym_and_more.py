# Generated by Django 4.0 on 2022-01-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Synonyms',
            new_name='Synonym',
        ),
        migrations.AddConstraint(
            model_name='synonym',
            constraint=models.UniqueConstraint(fields=('name', 'place'), name='synonym_name_place_key'),
        ),
    ]
