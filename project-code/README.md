# Deployable Cloudmesh Containers

## Authors

- Tim Whitson
- Gregor von Laszewski

## Motivation

- To standardize deployment of Docker containers running REST APIs. 
- To simplify the development of new APIs using custom interpreters and resolvers. Each REST API is defined simply using a YAML file and OpenAPI 2.0 (formerly Swagger) specification and a (Python) controller.

## Usage

...

## APIs

Each API will have a self-named subdirectory in the **apis** directory. The configuration file contains a list of desired APIs to run, by name. So, for example, the *store* API has the directory *apis/store* and can be called up with

    apis:
      - services
      
in the configuration file.

### Structure

Each API uses the following structure:

    .
    ├── swagger.yml         # Swagger specification
    ├── requirements.txt    # Python requirements
    ├── packages.txt        # Ubuntu package requirements
    └── controllers         # directory containing python controllers for API
        └── ...
        
- **swagger.yml** this file contains the swagger specification, for this API only (paths, definitions, etc.).
- **requirements.txt** newline-separated list of python package requirements, to be installed via *pip install*
- **pakackages.txt** newline-separated list of ubuntu package requirements, to be installed via *apt-get install*
- **controllers/** this directory is where the API controllers will be placed, with name corresponding to the path (see [Routing](#routing))

### Routing

CMENV uses a custom resolver, cmresolver. This resolver will create a route to each API by name, and each path. Using key store as an example. Each swagger path is maintained with the name of the API, the path, and the method (GET with no parameters defaults to SEARCH, in keaaping with the connexion default:

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

- [ ] prevent conflicting python packages

