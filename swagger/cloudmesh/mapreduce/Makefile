SWAGGER=java -jar swagger-codegen-cli-2.3.1.jar
SPEC=swagger.yml

all: 
	generate requirements run
	
codegen:
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar

generate:
	$(SWAGGER) generate \
		-i $(SPEC) \
		-l python-flask \
		-o server/mapreduce/flaskConnexion \
		-D supportPython2=true
	cp *_controller.py server/mapreduce/flaskConnexion/swagger_server/controllers/  

run:
	cd server/mapreduce/flaskConnexion/ &&\
	python -m swagger_server

requirements:
	pip install -r requirements.txt
	cd server/mapreduce/flaskConnexion; pip install -r requirements.txt
	
curl:
	curl -H "Content-Type: application/json" \
		-X POST \
		-d '{"words":"I I went to the the park"}' \
		http\://localhost\:8080/map      
	curl -H "Content-Type: application/json" \
		-X POST \
		-d '{"words":"I I went to the the park"}' \
		http\://localhost\:8080/reduce
		
docker-build:
	docker build -t cloudmesh-mapreduce .

docker-start:
	docker run -t -p 8080:8080 cloudmesh-mapreduce

clean:
	rm -rf server/
