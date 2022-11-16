FROM ubuntu
RUN apt update
RUN apt install python3 -y
RUN apt install python3-flask -y
COPY pag2.py /myapp/pag2.py
WORKDIR /myapp/
CMD python3 /myapp/pag2.py