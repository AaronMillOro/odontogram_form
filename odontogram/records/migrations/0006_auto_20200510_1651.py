# Generated by Django 3.0.5 on 2020-05-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20200510_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouth',
            name='t_11',
            field=models.ManyToManyField(blank=True, related_name='t11', to='records.Proceeding'),
        ),
    ]
