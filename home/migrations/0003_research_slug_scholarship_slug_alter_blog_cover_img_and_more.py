# Generated by Django 4.2.1 on 2023-05-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_update_datt_base_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='blog/cover-img'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog/img'),
        ),
    ]
