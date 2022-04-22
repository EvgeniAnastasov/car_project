# Generated by Django 4.0.3 on 2022-04-04 18:01

import cars.web_cars.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_cars', '0003_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[cars.web_cars.validators.MaxFileSizeInMbValidator(10)]),
        ),
    ]
