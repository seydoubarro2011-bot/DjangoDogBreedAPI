from django.db import models

# This is where I create my models.

from django.core.validators import MinValueValidator, MaxValueValidator


# This model stores information about different dog breeds.
class Breed(models.Model):

    # These are the allowed breed sizes.
    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]

    name = models.CharField(max_length=100)

    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES
    )

    # These fields must have values between 1 and 5.
    friendliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    trainability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    sheddingamount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    exerciseneeds = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    # This displays the breed name when viewing the record.
    def __str__(self):
        return self.name


# This model stores information about individual dogs.
class Dog(models.Model):

    name = models.CharField(max_length=100)

    age = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    # Each dog must belong to a breed.
    breed = models.ForeignKey(
        Breed,
        on_delete=models.PROTECT,
        related_name='dogs'
    )

    gender = models.CharField(max_length=20)

    color = models.CharField(max_length=50)

    favoritefood = models.CharField(max_length=100)

    favoritetoy = models.CharField(max_length=100)

    # This displays the dog's name when viewing the record.
    def __str__(self):
        return self.name
