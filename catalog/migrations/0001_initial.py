# Generated by Django 3.0.3 on 2020-02-13 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=512)),
                ('photo', models.FileField(upload_to='goods_photo/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Producer')),
            ],
        ),
    ]
