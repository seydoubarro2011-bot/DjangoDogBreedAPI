# Import Django REST Framework tools
from rest_framework import viewsets, status
from rest_framework.response import Response

# Import Django's protected deletion exception
from django.db.models.deletion import ProtectedError

# Import our models
from .models import Dog, Breed

# Import our serializers
from .serializers import DogSerializer, BreedSerializer


# Dog ViewSet
# Handles GET, POST, PUT, PATCH, and DELETE for dogs
class DogViewSet(viewsets.ModelViewSet):

    queryset = Dog.objects.all()
    serializer_class = DogSerializer


# Breed ViewSet
# Handles GET, POST, PUT, PATCH, and DELETE for breeds
class BreedViewSet(viewsets.ModelViewSet):

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    # Override the default DELETE behavior
    def destroy(self, request, *args, **kwargs):

        # Find the breed using its ID
        breed = self.get_object()

        try:
            # Attempt to delete the breed
            breed.delete()

        except ProtectedError:
            # Return an error if dogs are associated with the breed
            return Response(
                {
                    "error": "Cannot delete this breed because dogs are associated with it."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Return success if deletion was successful
        return Response(status=status.HTTP_204_NO_CONTENT)