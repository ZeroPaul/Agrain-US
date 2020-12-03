# Generated by Django 2.2.4 on 2019-10-04 13:41

import api.grain.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grain', '0003_auto_20191004_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampledetailgrain',
            name='sample',
            field=models.ForeignKey(default='7ef8e0fb-358d-4ebe-841a-259949ba3211', on_delete=django.db.models.deletion.CASCADE, related_name='detail_sample', to='grain.SampleGrain'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sampledetailgrain',
            name='image_result',
            field=models.ImageField(blank=True, upload_to=api.grain.models.sample_detail_path),
        ),
    ]
