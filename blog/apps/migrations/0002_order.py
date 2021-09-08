# Generated by Django 3.2 on 2021-08-26 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('priceUnit', models.IntegerField()),
                ('total', models.IntegerField()),
                ('customerName', models.CharField(max_length=50)),
                ('customerPhone', models.CharField(max_length=20)),
                ('customerAddress', models.CharField(max_length=200)),
                ('orderDate', models.DateTimeField()),
                ('deliverDate', models.DateTimeField(null=True)),
                ('status', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apps.product')),
            ],
        ),
    ]
