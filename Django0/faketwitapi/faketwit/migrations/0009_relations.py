# Generated by Django 4.0.3 on 2022-03-11 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faketwit', '0008_alter_tweets_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('followed',),
            },
        ),
    ]
