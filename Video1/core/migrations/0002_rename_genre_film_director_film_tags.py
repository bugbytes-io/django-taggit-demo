# Generated by Django 4.0.2 on 2022-02-08 18:23

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='genre',
            new_name='director',
        ),
        migrations.AddField(
            model_name='film',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
