# Generated by Django 4.0 on 2022-02-02 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_editor_edition_addition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
