# Generated by Django 5.1 on 2024-08-08 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcingapp', '0003_remove_news_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]