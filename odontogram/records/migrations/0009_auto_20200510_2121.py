# Generated by Django 3.0.5 on 2020-05-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20200510_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mouth',
            name='t_11',
        ),
        migrations.AddField(
            model_name='mouth',
            name='t_11',
            field=models.CharField(default='good', max_length=50),
        ),
        migrations.DeleteModel(
            name='Proceeding',
        ),
    ]