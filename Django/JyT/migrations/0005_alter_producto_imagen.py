# Generated by Django 5.0.6 on 2024-07-05 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JyT', '0004_remove_carritoitem_carrito_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='no_imagen.png', upload_to='productos'),
        ),
    ]