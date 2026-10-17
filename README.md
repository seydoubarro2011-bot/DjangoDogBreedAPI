# Django Dog and Breed REST API

## Project Description

This project is a Django REST API that I created for my
Secure Web Application Development lab.

The application allows users to create, retrieve, update,
and delete information about dogs and dog breeds.

I used Django, Django REST Framework, Python, and SQLite.

## Models

### Dog
- name
- age
- breed
- gender
- color
- favoritefood
- favoritetoy

### Breed
- name
- size
- friendliness
- trainability
- sheddingamount
- exerciseneeds

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/dogs/ | List dogs |
| POST | /api/dogs/ | Create dog |
| GET | /api/dogs/1/ | Retrieve dog |
| PUT | /api/dogs/1/ | Update dog |
| DELETE | /api/dogs/1/ | Delete dog |
| GET | /api/breeds/ | List breeds |
| POST | /api/breeds/ | Create breed |
| GET | /api/breeds/1/ | Retrieve breed |
| PUT | /api/breeds/1/ | Update breed |
| DELETE | /api/breeds/1/ | Delete breed |

## Installation

Clone the repository:

```cmd
git clone REPOSITORY_URL
```

Open the project folder:

```cmd
cd DjangoDogBreedAPI
```

Create a virtual environment:

```cmd
python -m venv venv
```

Activate the environment:

```cmd
venv\Scripts\activate
```

Install dependencies:

```cmd
pip install -r requirements.txt
```

Apply migrations:

```cmd
python manage.py migrate
```

Start the server:

```cmd
python manage.py runserver
```

## Testing

I used Postman to test all required HTTP methods.

The tests include:

- GET list
- POST
- GET detail
- PUT
- DELETE

I completed these tests for both the Dog and Breed models.

Screenshots are included in the screenshots folder.

## Implementation

I used class-based API views.

The four controller classes are:

- DogList
- DogDetail
- BreedList
- BreedDetail

## Author

Seydou Barro