FROM ubuntu

RUN apt-get update
RUN apt-get install -qy \
    python3-pip \
    git

RUN mkdir ~/cloudmesh
WORKDIR ~/cloudmesh

COPY config.yml .

RUN git clone https://github.com/cloudmesh-community/hid-sp18-526.git

RUN cd hid-sp18-526/project-code && pip3 install .

RUN cp hid-sp18-526/project-code/install.py .

RUN python3 install.py

EXPOSE 8080

CMD cmenv
