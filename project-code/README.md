# Deployable Cloudmesh Containers

## Authors

- Tim Whitson
- Gregor von Laszewski

## Motivation

- To standardize deployment of Docker containers running REST APIs. 
- To simplify the development of new APIs using custom interpreters and resolvers. Each REST API is defined simply using a YAML file and OpenAPI 2.0 (formerly Swagger) specification and a (Python) controller.

## Usage

Each working CMENV directory should be structured as follows:

    .
    ├── config.yml          # configuration file
    └── Dockerfile          # Dockerfile

- **config.yml** yaml configuration file. See [example](config.yml).
- **Dockerfile** Dockerfile. This should not be changed by the user.

Build Docker image:

    docker build -t cmenv .
    
Run Docker image:

    docker run -t -p 8080:8080 cmenv
    
-t enables ctrl+c closing of server and -p ensures the port is open to communicate with the server in the container.

## APIs

Each API will have a self-named subdirectory in the **apis** directory. The configuration file contains a list of desired APIs to run, by name. So, for example, the *store* API has the directory *apis/store* and can be called up with

    apis:
      - services
      
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
- **requirements.txt** newline-separated list of python package requirements, to be installed via *pip install*
- **pakackages.txt** newline-separated list of ubuntu package requirements, to be installed via *apt-get install*
- **controllers** directory where the API controllers will be placed, with name corresponding to the path (see [Routing](#routing))

### Routing

CMENV uses a custom resolver, cmresolver. This resolver will create a route to each API by name, and each path. Each swagger path is maintained with the name of the API, the path, and the method (GET with no parameters defaults to SEARCH, in keeping with the connexion default.

Key-value store example:

```yaml

    paths:
      /key:
        get:
          # routed to: apis.store.controllers.store.search

      '/key/{key}/{value}':
        get:
          # routed to: apis.store.controllers.store.get
```

Services example:

```yaml

    paths:
      /services:
        get:
          # routed to: apis.services.controllers.services
```

## Issues/to-do

- [ ] prevent conflicting python dependencies

