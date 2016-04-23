FROM docker.io/python:2.7
RUN apt-get  update && apt-get -y install python-pip 
ADD . /code
WORKDIR /code
RUN pip install -U pip
RUN pip install -rrequirements.txt
CMD python app.py
