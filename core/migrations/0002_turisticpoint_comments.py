# Generated by Django 2.0.13 on 2021-06-26 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turisticpoint',
            name='comments',
            field=models.ManyToManyField(to='comments.Comment'),
        ),
    ]
