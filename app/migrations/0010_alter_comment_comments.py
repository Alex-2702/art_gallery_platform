# Generated by Django 5.0 on 2024-01-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_comment_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments',
            field=models.TextField(),
        ),
    ]
