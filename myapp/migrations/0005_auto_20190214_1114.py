# Generated by Django 2.0.13 on 2019-02-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190213_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Reason_delay',
            field=models.TextField(default='', null=True),
        ),
    ]
