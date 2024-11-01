# Generated by Django 5.0.4 on 2024-10-23 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land_management', '0008_alter_detail_deed_number_alter_detail_file_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyCode', models.CharField(max_length=5)),
                ('CompanyName', models.CharField(max_length=8)),
            ],
        ),
        migrations.AlterField(
            model_name='detail',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_management.company'),
        ),
    ]
