# About the project
The main purpose of this project is have an API service that could be called by other HTTP services to check if certain URLs contains malwares and are not safe to call. The service will host all the URLs in a Database (Cosmos DB) and notify the callers of the service if the URL it's calling is safe or not. The service also has another endpoint which could be used to add URLs that contain malwares.  
The service is containerized using Docker and uses [`tiangolo/uvicorn-gunicorn`](https://hub.docker.com/r/tiangolo/uvicorn-gunicorn) image.

## Architecture 
![GitHub Logo](/assets/Architecture-diagram.png)


- **Database**: [Azure Cosmos](https://azure.microsoft.com/en-us/services/cosmos-db/) database
- **API**: Python FastApi framework 

## Endpoints 
Below are the endpoints in this project: 
- `GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}`  
-- This endpoint will check whether the passed URL contains malware. 
- `POST /url-insert/1`  
-- This endpoint will insert URL(s) to the database. It has the ability to take more than one URL.  
- `GET /doc`  
-- Returns the swagger document generated from FastApi
- `GET /`  
-- Health endpoint that returns `True` if the service is up and running

Detailed information can be found in the Swagger doc under `assets` folder.   

## Files Structure 
```
├── Dockerfile                        <- The docker file for this project.
├── Makefile                          <- Make file used for the project
├── .gitignore                        <- Git ignore file.
├── README.md                         <- The README file containing information for using the project.
├── requirements.txt                  <- Contains all the python libraries used 
├── app                               <- Project source files.
|   |
│   ├── common                        <- Common functionality that could be extracted to a library.
│   │   └── cosmos_client_manager.py  <- Cosmos database client manager.  
|   |
│   ├── dto                           <- Data transfer objects (pydantic models).
│   │   └── url_lookup_response.py    
|   |
│   ├── providers                     <- Provider clients for external APIs/Database/Services.
│   │   └── url_info_provider.py      
|   |
│   ├── services                      <- Services to expose providers.
│   │   └── url_info_service.py
│   | 
|   ├── constants.py                  <- Contains constant values shared across the project
|   |
│   └── main.py                       <- Entry point for the code 
|
├── assets                            <- Contains diagrams and swagger docs
|   
└── tests                             <- Project tests.
    |
    ├── integration                   <- Integration tests.
    |
    └── unit                          <- Unit tests.
        └── test_url_info_provider.py
```


# Getting Started
Below are the prerequisite tools needed to run the service: 
* [Docker](https://docs.docker.com/get-docker/)
* [Make](https://www.gnu.org/software/make/)

## Running the Service 
Below are the steps to the run the service locally: 
1. Create a `.env` file in the root directory with the contents below:  
`COSMOS_DB_MASTER_KEY=<Databse-key>`  
`APP_INSIGHTS_CONNECTION_STRING=<Application-insights-key>`
(this will contain the database secret key and application insights key)
2. In the root directory, run `make local-deploy`. It will run the linting, tests and builds the application in a docker container. 
3. The service will be running in `http://localhost:3002`. You can now hit the service using your tool of choice. Make sure to insert `Api-key` parameter for authentication 
4. The service uses keys for authentication, so make sure to insert `Api-key` in your request before calling  the service

Alternatively, the service can be ran in the cloud using Azure Web Apps: 
1. In the root directory, run `make remote-deploy`. This step will push the Docker image to Azure Container registery.
2. Once the image is successfully pushed, Azure Web App will pick up the latest docker image. 
3. The service will be running in `https://url-lookup-east-service.azurewebsites.net/`. 
4. The service uses keys for authentication, so make sure to insert `Api-key` in your request before calling  the service

Sample postman collection can be found under `assets` folder)

## Testing
The service currently has Unit tests implemented. Below are the steps to run the tests:
1. Create a `.env` file in the root directory with the contents below:  
`COSMOS_DB_MASTER_KEY=<Databse-key>`  
(this will contain the database secret key)
2. In the root directory, run `make tests`. This will run only the tests implemented and will fail if any tests do not pass. 


# Future Enhancements
1. Endpoint for deleting URLs from the Database 
2. Integration tests 
3. Integrating CICD tool