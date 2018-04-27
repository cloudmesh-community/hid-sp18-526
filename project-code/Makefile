docker-build:
	docker build -t cmenv example/
	
docker-run:
	docker run -t -p 8080:8080 cmenv
	
test:
	curl -X GET localhost:8080/services
	curl -X PUT localhost:8080/key/test/hi
	curl -X GET localhost:8080/key
