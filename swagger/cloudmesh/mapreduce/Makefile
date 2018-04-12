SWAGGER=java -jar swagger-codegen-cli-2.3.1.jar
SPEC=swagger.yml

all: generate requirements run
	@echo "DONE"

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

clean:
	rm -rf server/
