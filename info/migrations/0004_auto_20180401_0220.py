# Generated by Django 2.0.3 on 2018-03-31 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20180401_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='pincode',
            field=models.CharField(max_length=10),
        ),
    ]