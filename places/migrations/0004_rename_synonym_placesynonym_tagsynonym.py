# Generated by Django 4.0 on 2022-01-18 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_synonym_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Synonym',
            new_name='PlaceSynonym',
        ),
        migrations.CreateModel(
            name='TagSynonym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=500, unique=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='places.tag')),
            ],
        ),
    ]
