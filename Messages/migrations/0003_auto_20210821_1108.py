# Generated by Django 3.2.6 on 2021-08-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages', '0002_product_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('reciever', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('subject', models.CharField(max_length=50)),
                ('creation_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
