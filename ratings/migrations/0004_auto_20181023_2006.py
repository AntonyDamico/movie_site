# Generated by Django 2.1.1 on 2018-10-24 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20181019_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrating',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
    ]