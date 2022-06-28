# Generated by Django 2.2.5 on 2022-06-28 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20220628_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productspecificationvalue',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_value_product', to='product.Product'),
        ),
        migrations.AlterField(
            model_name='productspecificationvalue',
            name='specification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.ProductSpecification'),
        ),
    ]
