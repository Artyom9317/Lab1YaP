# Generated by Django 2.2.6 on 2019-10-30 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OEApp', '0005_auto_20191031_0447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='path',
        ),
    ]
