# Generated by Django 2.2 on 2020-12-02 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_last', '0007_auto_20201203_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner_up',
            old_name='image',
            new_name='banner_im',
        ),
    ]
