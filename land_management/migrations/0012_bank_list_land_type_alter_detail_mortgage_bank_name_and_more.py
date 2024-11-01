# Generated by Django 5.0.4 on 2024-10-24 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land_management', '0011_detail_khajana_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Land_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='detail',
            name='mortgage_bank_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_management.bank_list'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='type_of_land',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_management.land_type'),
        ),
    ]
