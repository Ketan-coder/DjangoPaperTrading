# Generated by Django 4.1.6 on 2023-08-09 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Commodity', '0001_initial'),
        ('Options', '0006_alter_option_lastprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='CommodityUnderlying',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Commodity.commodity'),
        ),
    ]
