# Generated by Django 4.0.2 on 2023-03-04 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]