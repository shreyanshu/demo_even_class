# Generated by Django 3.0.7 on 2020-06-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen_managemant_system', '0004_auto_20200625_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('cook', models.ManyToManyField(to='canteen_managemant_system.Cook')),
            ],
        ),
    ]