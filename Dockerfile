FROM docker.io/python:2.7
RUN echo deb http://ftp.it.debian.org/debian jessie main > /etc/apt/sources.list
RUN apt-get  update && apt-get -y install python-pip libnss-extrausers && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN sed -i 's/passwd:         compat/passwd:         compat extrausers/' /etc/nsswitch.conf
RUN echo "python2:x:1000160000:1000160000:Python Server:/code:/bin/bash" >> /var/lib/extrausers/passwd
RUN chmod a+w /var/lib/extrausers/passwd
ADD . /code
WORKDIR /code
RUN pip install -U pip
RUN pip install -rrequirements.txt
EXPOSE 8080
CMD bash /code/entrypoint.sh
