# Generated by Django 5.0.6 on 2024-05-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JyT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='pass1', max_length=30),
            preserve_default=False,
        ),
    ]
