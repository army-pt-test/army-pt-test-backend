# Generated by Django 4.0.2 on 2022-02-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('army_pt_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadet',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='cadet',
            name='middleinitial',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
