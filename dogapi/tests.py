from django.test import TestCase
from rest_framework.test import APIClient

from .models import Breed, Dog


class BreedAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.breed_data = {
            "name": "Golden Retriever",
            "size": "Large",
            "friendliness": 5,
            "trainability": 5,
            "sheddingamount": 4,
            "exerciseneeds": 5,
        }

    def test_create_breed(self):
        response = self.client.post(
            "/api/breeds/",
            self.breed_data,
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Breed.objects.count(), 1)
        self.assertEqual(
            Breed.objects.get().name,
            "Golden Retriever",
        )

    def test_list_breeds(self):
        Breed.objects.create(**self.breed_data)

        response = self.client.get("/api/breeds/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["name"],
            "Golden Retriever",
        )


class DogAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.breed = Breed.objects.create(
            name="Golden Retriever",
            size="Large",
            friendliness=5,
            trainability=5,
            sheddingamount=4,
            exerciseneeds=5,
        )

        self.dog_data = {
            "name": "Buddy",
            "age": 3,
            "breed": self.breed.pk,
            "gender": "Male",
            "color": "Golden",
            "favoritefood": "Chicken",
            "favoritetoy": "Ball",
        }

    def test_create_dog(self):
        response = self.client.post(
            "/api/dogs/",
            self.dog_data,
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Dog.objects.count(), 1)
        self.assertEqual(
            Dog.objects.get().name,
            "Buddy",
        )

    def test_list_dogs(self):
        Dog.objects.create(
            name="Buddy",
            age=3,
            breed=self.breed,
            gender="Male",
            color="Golden",
            favoritefood="Chicken",
            favoritetoy="Ball",
        )

        response = self.client.get("/api/dogs/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["name"],
            "Buddy",
        )