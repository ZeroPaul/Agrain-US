# Generated by Django 2.2.4 on 2019-10-31 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grain', '0010_catergorygrain'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CatergoryGrain',
            new_name='CategoryGrain',
        ),
        migrations.AlterModelOptions(
            name='categorygrain',
            options={'ordering': ['name'], 'verbose_name': 'Category Grain', 'verbose_name_plural': 'Categories Grains'},
        ),
    ]
