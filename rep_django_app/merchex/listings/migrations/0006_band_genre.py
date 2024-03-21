# Generated by Django 5.0.3 on 2024-03-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_remove_band_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock')], default='HH', max_length=50),
            preserve_default=False,
        ),
    ]
