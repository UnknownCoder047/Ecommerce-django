# Generated by Django 4.1 on 2023-05-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_no',
            field=models.CharField(default=12345, max_length=10),
            preserve_default=False,
        ),
    ]