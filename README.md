# DATA-API

## Quick presentation
This API is the BFF for the front-qa application.

## Technologies
- Python
- Flask
- Docker
- remidqa quality workflow
- Pymongo

## Build
- This API is designed for a Docker usage
- To build simple run : ```docker build -t {tag-name} .```
- Then the image will be available on your local repository

## Configuration
- To communicate with the data stored in a mongo-db atlas : set en variable ```MONGODB_SRV```

## Usage
- just few ```[GET]```, ```[POST]```, ```[DELETE]``` and ```[PUT]``` routes to CRUD over some data needed in the front-qa website
- For deployment and testing, this repository uses the [remidqa/build-deploy-test](https://github.com/remidqa/qa-configurations/blob/main/.github/workflows/build-deploy-test.yml) quality workflow

