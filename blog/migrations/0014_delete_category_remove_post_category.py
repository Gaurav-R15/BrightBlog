# Generated by Django 4.0.2 on 2023-03-08 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]