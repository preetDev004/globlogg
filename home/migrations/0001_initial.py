# Generated by Django 5.0.2 on 2024-02-28 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('ENTERTAINMENT', 'Entertainment'), ('BUSINESS', 'Business'), ('TECHNOLOGY', 'Technology'), ('FOOD', 'Food'), ('GAMES', 'Games')], default='ENTERTAINMENT', max_length=15)),
                ('img_url', models.URLField()),
                ('created_at', models.DateField()),
            ],
        ),
    ]
