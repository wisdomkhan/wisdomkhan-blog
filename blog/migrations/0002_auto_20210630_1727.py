# Generated by Django 3.2.4 on 2021-06-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribute',
            name='slug',
            field=models.TextField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contribute',
            name='text',
            field=models.TextField(default='', max_length=5000),
            preserve_default=False,
        ),
    ]