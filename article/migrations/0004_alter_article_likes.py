# Generated by Django 4.0.2 on 2022-04-20 09:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0003_alter_article_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
