# Generated by Django 2.2 on 2020-12-02 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_last', '0002_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gal_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
