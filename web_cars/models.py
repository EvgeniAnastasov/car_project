from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from cars.web_cars.validators import MaxFileSizeInMbValidator, CharAndNumsOnlyValidator

UserModel = get_user_model()


class Car(models.Model):
    TYPES = [
        (None, 'Choose Car Type'),
        ('sedan', 'sedan'),
        ('hatchback', 'hatchback'),
        ('convertable', 'convertable'),
        ('sport car', 'sport car'),
        ('estate', 'estate'),
        ('SUV', 'SUV'),
        ('VAN', 'VAN'),
        ('Other', 'Other'),
    ]

    ENGINES = [
        (None, 'Choose Engine Type'),
        ('petrol', 'petrol'),
        ('diesel', 'diesel'),
        ('EV', 'EV'),
        ('hybrid', 'hybrid'),
    ]

    TRANSMISSIONS = [
        (None, 'Choose Transmission Type'),
        ('manual', 'manual'),
        ('auto', 'auto')
    ]

    car_brand = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(1),
            CharAndNumsOnlyValidator,
        ),
    )

    car_model = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(2),
            CharAndNumsOnlyValidator,
        ),
    )

    type = models.CharField(
        max_length=30,
        choices=TYPES,
    )

    engine = models.CharField(
        max_length=30,
        choices=ENGINES,
    )

    hp = models.IntegerField(

    )

    transmission = models.CharField(
        max_length=30,
        choices=TRANSMISSIONS,
    )

    year = models.IntegerField(

    )

    image = models.ImageField(
        upload_to='mediafiles/',
        # default='/static/car1.webp',
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(10),
        ),
    )

    mileage = models.IntegerField(
    )

    # user_profile = models.ForeignKey(
    #     Profile,
    #     on_delete=models.CASCADE,
    # )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.car_brand} {self.car_model}'

    class Meta:
        ordering = ('car_brand', 'car_model',)


class Like(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Photos(models.Model):
    car_photo = models.ImageField(
        upload_to='photos',
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(10),
        ),
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    car_id = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )

