# Generated by Django 4.0.3 on 2023-08-18 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_rename_autor_board_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
