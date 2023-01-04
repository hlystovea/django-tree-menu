FROM python:3.10
WORKDIR /tree_menu
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./project .
