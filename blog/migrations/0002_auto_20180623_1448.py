# Generated by Django 2.0.6 on 2018-06-23 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Published_date',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Title',
            new_name='title',
        ),
    ]
