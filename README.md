# About the project
The main purpose of this project is have an API service that could be called by other HTTP services to check if certain URLs contains malwares and are not safe to call. The service will host all the URLs in a Database (Cosmos DB) and notify the callers of the service if the URL it's calling is safe or not. The service also has another endpoint which could be used to add URLs that contain malwares

## Architecture 
Below is the high-level architecture diagram for the service: 
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
1. Create a `.env` file in the root directory. This will contain the database secret key.
2. In the root directory, run `make local-deploy`. It will run the tests and builds the application in a docker container. 
3. The service will be running in `http://localhost:3002`. You can now hit the service using your tool of choice (Sample postman collection can be found under `assest` folder)

# Future Enhancements
1. Endpoint for deleting URLs from the Database 
2. Integration tests 
3. Integrating CICD tool