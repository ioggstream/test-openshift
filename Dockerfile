FROM docker.io/python:2.7
RUN echo deb http://ftp.it.debian.org/debian jessie main > /etc/apt/sources.list
RUN apt-get  update && apt-get -y install python-pip libnss-extrausers && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN sed -i 's/passwd:         compat/passwd:         compat extrausers/' /etc/nsswitch.conf
ADD . /code
WORKDIR /code
RUN pip install -U pip
RUN pip install -rrequirements.txt
CMD bash /code/entrypoint.sh
