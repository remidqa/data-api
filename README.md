# README

## Used Technologies
- Python API
- Docker
- Mongodb Atlas

## What is this application for
A simple API to ba able to make some CRUD tests scenarios.
It store "FAQ Entries" in a database with the following format : 
```json
{
    "en": {
        "title": "English title for the FAQ Entry",
        "description": "English description for the FAQ Entry"
    },
    "fr": {
        "title": "Titre française de la section de la FAQ",
        "description": "Description française de la section de la FAQ"
    }
}
```

## Setup
The easiest way to run the API is to build a Docker container and run it
first set up some variables (either in a ```.env``` or ```Dockerfile``` file): 
- ```MONGODB_SRV``` : SRV path to connect to a mongodb atlas dadabase

## Build
- ```docker build -t faq-api```
- ```docker run newman-runner```

## Paths
- ```[GET] /faq``` : Get all faq entries
- ```[POST] /faq``` : Create a new entry
  - expexted body example : 
    ```json
    {
        "en": {
            "title": "English title for the FAQ Entry",
            "description": "English description for the FAQ Entry"
        },
        "fr": {
            "title": "Titre française de la section de la FAQ",
            "description": "Description française de la section de la FAQ"
        }
    }
    ```
- ```[GET] /faq/id/:id``` : Get a faq entry by its database ID
- ```[PUT] /faq/id/:id``` : Update a faq entry by its database ID
  - expected body example :
  ```json
  {"en.title": "new updated title for FAQ entry"}
  ```
- ```[DELETE] /faq/id/:id``` : Delete one FAQ entry