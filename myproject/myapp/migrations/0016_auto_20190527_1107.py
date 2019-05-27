# Generated by Django 2.2 on 2019-05-27 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_sumstock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.Material'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Restaurant'),
        ),
    ]
