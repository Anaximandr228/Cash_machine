FROM ubuntu:latest

RUN apt update
RUN apt install wkhtmltopdf
RUN apt install python3 python3-pip -y
RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt


COPY . .