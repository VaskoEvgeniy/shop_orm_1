# Generated by Django 4.1 on 2022-09-13 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0003_tenant_is_active_alter_tenant_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32)),
                ('category_slug', models.SlugField(max_length=32)),
                ('category_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=32)),
                ('product_slug', models.SlugField(max_length=32)),
                ('product_description', models.TextField(blank=True, null=True)),
                ('product_cost', models.PositiveIntegerField(default=0)),
                ('availability', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='tenant',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]