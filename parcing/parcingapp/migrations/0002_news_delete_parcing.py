# Generated by Django 5.1 on 2024-08-08 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('link', models.URLField()),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('visibility', models.CharField(max_length=12, null=True)),
                ('published_at', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Parcing',
        ),
    ]
