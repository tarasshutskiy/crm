# Generated by Django 4.2.1 on 2023-05-12 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_statuscrm_order_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment_name', models.TextField(verbose_name='Text comment')),
                ('coment_dt', models.DateTimeField(auto_now=True, verbose_name='Date create')),
                ('coment_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order', verbose_name='Application')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
