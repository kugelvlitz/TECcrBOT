# Generated by Django 4.0 on 2022-02-06 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_remove_page_page_id_type_unique_alter_page_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='mtime',
            field=models.DateField(null=True),
        ),
    ]
