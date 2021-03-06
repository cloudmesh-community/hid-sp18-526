# Deployable Cloudmesh Containers

## Authors

- Tim Whitson
- Gregor von Laszewski

## Motivation

- To standardize deployment of Docker containers running REST APIs. 
- To simplify the development of new APIs using custom interpreters and resolvers. Each REST API is defined simply using a YAML file and OpenAPI 2.0 (formerly Swagger) specification and a (Python) controller.

## Test Run (using make)

Build container from example:

    make docker-build
    
Run container:

    make docker-run
    
Test services and key store:

    make test

## Usage

Each working CMENV directory should be structured as follows:

    .
    ├── config.yml          # configuration file
    └── Dockerfile          # Dockerfile

- **config.yml** yaml configuration file. See [example](examples/config.yml).
- **Dockerfile** Dockerfile. This should not be changed by the user (copy the Dockerfile from this repository).

Build Docker image:

    docker build -t cmenv .
    
Run Docker image:

    docker run -t -p 8080:8080 cmenv
    
-t enables ctrl+c closing of server and -p ensures the port is open to communicate with the server in the container.

Make sure server is running properly:

    curl -X GET localhost:8080/services

## APIs

Each API will have a self-named subdirectory in the **apis** directory. The configuration file contains a list of desired APIs to run, by name. So, for example, the *store* API has the directory *apis/store* and can be called up with

    apis:
      - store
      
in the configuration file.

### Structure

Each API uses the following structure:

    .
    ├── swagger.yml         # swagger specification
    ├── requirements.txt    # python requirements
    ├── packages.txt        # ubuntu package requirements
    └── controllers         # directory containing python controllers for API
        └── ...
        
- **swagger.yml** this file contains the swagger specification, for this API only (paths, definitions, etc.).
- **requirements.txt** newline-separated list of python package requirements, to be installed via *pip3 install* (currently all packages use Python 3)
- **pakackages.txt** newline-separated list of ubuntu package requirements, to be installed via *apt-get install*
- **controllers** directory where the API controllers will be placed, with name corresponding to the path (see [Routing](#routing))

## Routing

CMENV uses a custom resolver, cmresolver. This resolver will create a route to each API by name, and each path. Each swagger path is maintained with the name of the API, the path, and the method (GET with no parameters defaults to SEARCH, in keeping with the connexion default.

Key-value store example, from [store swagger file](apis/store/swagger.yml):

```yaml

    paths:
      /key:
        get:
          # routed to: apis.store.controllers.store.search
          
      '/key/{key}':
        get:
          # routed to: apis.store.controllers.store.get  
        delete:
          # routed to: apis.store.controllers.store.delete

      '/key/{key}/{value}':
        put:
          # routed to: apis.store.controllers.store.put
```

## Issues/to-do

- [ ] prevent conflicting python dependencies
- [ ] prevent conflicting API endpoints
- [ ] auto-reloading when services enabled/disabled
- [ ] list of services/endpoints

