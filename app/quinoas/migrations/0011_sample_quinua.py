# Generated by Django 2.2.4 on 2019-09-26 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quinoas', '0010_sample_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='quinua',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='QuinuaM', to='quinoas.Quinua'),
            preserve_default=False,
        ),
    ]
