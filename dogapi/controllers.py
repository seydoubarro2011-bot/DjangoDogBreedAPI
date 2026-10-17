from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError

from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


# =====================================================
# DOG LIST
# Handles GET and POST requests for /api/dogs/
# =====================================================

class DogList(APIView):

    # GET returns all dogs stored in the database.
    def get(self, request):

        dogs = Dog.objects.all()

        serializer = DogSerializer(dogs, many=True)

        return Response(serializer.data)


    # POST creates a new dog.
    def post(self, request):

        serializer = DogSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =====================================================
# DOG DETAIL
# Handles GET, PUT, and DELETE for one dog.
# =====================================================

class DogDetail(APIView):

    # GET returns one dog using its ID.
    def get(self, request, pk):

        dog = get_object_or_404(Dog, pk=pk)

        serializer = DogSerializer(dog)

        return Response(serializer.data)


    # PUT updates an existing dog.
    def put(self, request, pk):

        dog = get_object_or_404(Dog, pk=pk)

        serializer = DogSerializer(
            dog,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # DELETE removes a dog from the database.
    def delete(self, request, pk):

        dog = get_object_or_404(Dog, pk=pk)

        dog.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


# =====================================================
# BREED LIST
# Handles GET and POST requests for /api/breeds/
# =====================================================

class BreedList(APIView):

    # GET returns all breeds.
    def get(self, request):

        breeds = Breed.objects.all()

        serializer = BreedSerializer(
            breeds,
            many=True
        )

        return Response(serializer.data)


    # POST creates a new breed.
    def post(self, request):

        serializer = BreedSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =====================================================
# BREED DETAIL
# Handles GET, PUT, and DELETE for one breed.
# =====================================================

class BreedDetail(APIView):

    # GET returns one breed.
    def get(self, request, pk):

        breed = get_object_or_404(Breed, pk=pk)

        serializer = BreedSerializer(breed)

        return Response(serializer.data)


    # PUT updates an existing breed.
    def put(self, request, pk):

        breed = get_object_or_404(Breed, pk=pk)

        serializer = BreedSerializer(
            breed,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # DELETE removes a breed.
    def delete(self, request, pk):

        breed = get_object_or_404(Breed, pk=pk)

        try:
            breed.delete()

        except ProtectedError:

            return Response(
                {
                    "error": "Cannot delete a breed that has dogs."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )