# Generated by Django 3.0.8 on 2020-08-29 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='id',
            new_name='msg_id',
        ),
    ]
