FROM ubuntu

RUN apt-get update
RUN apt-get install -qy \
    python-pip \
    python3-pip \
    git
    
RUN pip install fabric pyyaml
RUN pip3 install connexion

RUN mkdir ~/cloudmesh
WORKDIR ~/cloudmesh

# create data directory
RUN mkdir data

COPY config.yml .

RUN git clone https://github.com/cloudmesh-community/hid-sp18-526.git

RUN cd hid-sp18-526/project-code && pip3 install . && fab install 

EXPOSE 8080

CMD cmenv
