# Generated by Django 2.2 on 2019-05-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190524_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermaterial',
            name='datereturn',
            field=models.DateField(blank=True, null=True),
        ),
    ]
