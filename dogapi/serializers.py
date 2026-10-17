from rest_framework import serializers
from .models import Dog, Breed


# This serializer converts Breed records to and from JSON.
class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed

        # These are the fields returned by the API.
        fields = [
            'id',
            'name',
            'size',
            'friendliness',
            'trainability',
            'sheddingamount',
            'exerciseneeds'
        ]


# This serializer converts Dog records to and from JSON.
class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog

        fields = [
            'id',
            'name',
            'age',
            'breed',
            'gender',
            'color',
            'favoritefood',
            'favoritetoy'
        ]