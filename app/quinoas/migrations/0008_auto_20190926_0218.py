# Generated by Django 2.2.4 on 2019-09-26 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quinoas', '0007_sample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='broken_grain',
            field=models.DecimalField(decimal_places=9, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='sample',
            name='coated_grain',
            field=models.DecimalField(decimal_places=9, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='sample',
            name='damaged_grain',
            field=models.DecimalField(decimal_places=9, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='sample',
            name='germinated_grain',
            field=models.DecimalField(decimal_places=9, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='sample',
            name='immature_grain',
            field=models.DecimalField(decimal_places=9, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='sample',
            name='whole_grain',
            field=models.DecimalField(decimal_places=9, default=0.0, max_digits=9),
        ),
    ]
