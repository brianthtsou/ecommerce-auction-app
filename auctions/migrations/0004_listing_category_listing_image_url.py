# Generated by Django 4.2.2 on 2023-07-22 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_listing_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('FAS', 'Fashion'), ('TOY', 'Toys'), ('ELE', 'Electronics'), ('HOM', 'Home'), ('SPO', 'Sporting Goods'), ('TAP', 'Tools and Parts'), ('BKS', 'Books'), ('PET', 'Pet Supplies'), ('HLT', 'Health and Beauty'), ('MSC', 'Miscellaneous')], default='MSC', max_length=3),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_url',
            field=models.CharField(default='', max_length=2048),
        ),
    ]
