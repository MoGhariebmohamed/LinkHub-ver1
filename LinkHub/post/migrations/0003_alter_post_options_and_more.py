# Generated by Django 5.1 on 2024-08-25 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_attachment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='postattachment',
            old_name='imagge',
            new_name='image',
        ),
    ]
