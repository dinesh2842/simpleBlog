# Generated by Django 4.2.4 on 2023-08-21 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_category_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]