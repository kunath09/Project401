# Generated by Django 2.2 on 2019-05-07 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190502_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buymetprocess',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.MaterialItem'),
        ),
    ]
