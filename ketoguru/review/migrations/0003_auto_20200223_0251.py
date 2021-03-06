# Generated by Django 3.0.3 on 2020-02-23 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='review',
            name='detail',
            field=models.TextField(blank=True, verbose_name='Detail'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Image'),
        ),
    ]
