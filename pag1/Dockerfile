FROM ubuntu
RUN apt update
RUN apt install python3 -y
RUN apt install python3-flask -y
RUN apt-get install python3-pip -y
RUN pip3 install dash
RUN apt install docker-compose -y 
CMD docker build -t usuario /myapp/
CMD python3 /myapp/pag1.py