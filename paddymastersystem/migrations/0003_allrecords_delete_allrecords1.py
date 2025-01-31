# Generated by Django 5.0.4 on 2024-06-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paddymastersystem', '0002_remove_allrecords1_gennius_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('kl_no', models.CharField(max_length=100)),
                ('mill_name', models.CharField(max_length=100)),
                ('mill_place', models.CharField(max_length=100)),
                ('mill_rate', models.FloatField()),
                ('mill_weight', models.FloatField()),
                ('mill_remarks', models.TextField(blank=True, null=True)),
                ('mill_total_wages', models.FloatField()),
                ('party_name', models.CharField(max_length=100)),
                ('party_address', models.CharField(max_length=200)),
                ('party_weight', models.FloatField()),
                ('paddy_variety', models.CharField(max_length=100)),
                ('lorry_no', models.CharField(max_length=100)),
                ('lorry_advance', models.FloatField()),
                ('lorry_total_fare', models.FloatField()),
                ('gennius_qty', models.FloatField()),
                ('gennius_price', models.FloatField()),
                ('mill_calculation_type', models.CharField(choices=[('BAGS_X4', 'BAGS X 4'), ('78KGS', '78 KGS'), ('79KGS', '79 KGS'), ('79_Delivery', '79 Delivery'), ('78_Delivery', '78 Delivery'), ('BAGS_X4_Delivery', 'BAGS X 4 Delivery')], max_length=50)),
                ('mill_rate_type', models.CharField(choices=[('party rate', 'party rate'), ('mill rate', 'mill rate')], max_length=100)),
                ('party_calculation_type', models.CharField(choices=[('BAGS_X4', 'BAGS X 4'), ('78KGS', '78 KGS'), ('79KGS', '79 KGS'), ('79_Delivery', '79 Delivery'), ('78_Delivery', '78 Delivery'), ('BAGS_X4_Delivery', 'BAGS X 4 Delivery')], max_length=50)),
                ('party_rate_type', models.CharField(choices=[('mill rate', 'mill rate'), ('party rate', 'party rate')], max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='AllRecords1',
        ),
    ]
