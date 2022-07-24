# Generated by Django 4.0.6 on 2022-07-24 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
        ('ratings', '0002_rename_user_rating_app_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='song',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.song'),
        ),
    ]
