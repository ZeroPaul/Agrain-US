# Generated by Django 2.2.4 on 2019-10-04 02:26

import api.grain.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grain', '0002_auto_20191004_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sampledetailgrain',
            name='type_grain_detail',
        ),
        migrations.AlterField(
            model_name='analysisgrain',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis_sample', to='grain.SampleGrain'),
        ),
        migrations.AlterField(
            model_name='samplegrain',
            name='image',
            field=models.ImageField(upload_to=api.grain.models.sample_path),
        ),
    ]