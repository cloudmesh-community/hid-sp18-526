# Deployable Cloudmesh Containers

## Authors

- Tim Whitson
- Gregor von Laszewski

## Motivation

- To standardize deployment of Docker containers running REST APIs. 
- To simplify the development of new APIs using custom interpreters and resolvers. Each REST API is defined simply using a YAML file and OpenAPI 2.0 (formerly Swagger) specification and a (Python) controller.

## API Structure

    .
    ├── swagger.yml         # Swagger specification
    ├── requirements.txt    # Python requirements
    ├── packages.txt        # Ubuntu package requirements
    └── controllers         # directory containing python controllers for API
        └── ...

