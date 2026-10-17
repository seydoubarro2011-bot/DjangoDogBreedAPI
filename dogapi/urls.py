from django.urls import path

from .controllers import (
    DogList,
    DogDetail,
    BreedList,
    BreedDetail
)


# These URL patterns connect requests to API controllers.
urlpatterns = [

    # URLs for listing and creating dogs.
    path(
        'dogs/',
        DogList.as_view(),
        name='dog-list'
    ),

    # URLs for retrieving, updating, and deleting one dog.
    path(
        'dogs/<int:pk>/',
        DogDetail.as_view(),
        name='dog-detail'
    ),

    # URLs for listing and creating breeds.
    path(
        'breeds/',
        BreedList.as_view(),
        name='breed-list'
    ),

    # URLs for retrieving, updating, and deleting one breed.
    path(
        'breeds/<int:pk>/',
        BreedDetail.as_view(),
        name='breed-detail'
    ),

]