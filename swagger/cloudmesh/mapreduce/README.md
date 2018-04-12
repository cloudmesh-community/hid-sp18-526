# Swagger MapReduce Server

Retrieve swagger-codegen (skip this if running in Docker):

    wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar

To generate swagger service:

    make
    
To run swagger service:
    
    make run
    
To run in Docker:

    docker build cloudmesh-mapreduce .
    docker run -p 8080:8080 cloudmesh-mapreduce
    
To test:

    make curl
    
This is a simple implementation of MapReduce. Given a string, the *map* function will return each word in the string. The *reduce* function will return each unique word and the number of occurrences.

Map is at /map.
Reduce is at /reduce.

map:

    curl -H "Content-Type: application/json" \
    -X POST \
    -d '{"words":"I I went to the the park"}' \
    http://localhost:8080/map
    
    > [["I", 1], ["I", 1], ["went", 1], ["to", 1], ["the", 1], ["the", 1], ["park", 1]]
    
reduce:
    
    curl -H "Content-Type: application/json" \
    -X POST \
    -d '{"words":"I I went to the the park"}' \
    http://localhost:8080/reduce
    
    > {"I": 2, "to": 1, "went": 1, "park": 1, "the": 2}
