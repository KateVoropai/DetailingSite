# Generated by Django 5.0.6 on 2024-05-28 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_alter_category_name_category_alter_portfolio_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='describe_service',
            field=models.CharField(default='Описание', max_length=500, null=True, verbose_name='описание сервиса'),
        ),
        migrations.AlterField(
            model_name='price',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='about_us.category', verbose_name='категория'),
        ),
    ]
