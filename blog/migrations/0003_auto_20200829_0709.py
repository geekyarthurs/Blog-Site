# Generated by Django 3.0.7 on 2020-08-29 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200826_1739'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Quote1',
        ),
        migrations.DeleteModel(
            name='Quote2',
        ),
        migrations.DeleteModel(
            name='Quote3',
        ),
    ]
