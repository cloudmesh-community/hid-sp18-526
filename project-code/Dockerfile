FROM ubuntu

RUN apt-get -qy \
    python-pip3
    git

RUN mkdir ~/cloudmesh

COPY config.yml ~/cloudmesh

# pip install all from apis/*/requirements.txt
RUN find apis -name 'requirements.txt' -exec pip3 install -r {} \;

# install all packages from apis/*/packages.txt
#RUN find apis -name 'packages.txt' -exec cat {} \; | xargs apt-get install -y





EXPOSE 8080
