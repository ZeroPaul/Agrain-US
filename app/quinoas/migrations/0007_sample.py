# Generated by Django 2.2.4 on 2019-09-26 02:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quinoas', '0006_auto_20190925_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('image', models.ImageField(upload_to='samples/')),
                ('broken_grain', models.DecimalField(decimal_places=9, default=0.0, max_digits=20)),
                ('damaged_grain', models.DecimalField(decimal_places=9, default=0.0, max_digits=20)),
                ('immature_grain', models.DecimalField(decimal_places=9, default=0.0, max_digits=20)),
                ('coated_grain', models.DecimalField(decimal_places=9, default=0.0, max_digits=20)),
                ('germinated_grain', models.DecimalField(decimal_places=9, default=0.0, max_digits=20)),
                ('whole_grain', models.DecimalField(decimal_places=9, default=0.0, max_digits=20)),
            ],
            options={
                'verbose_name_plural': 'Sample',
                'ordering': ['uuid'],
            },
        ),
    ]
