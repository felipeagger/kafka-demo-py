FROM python:3.7

RUN mkdir -p /home/py/app

WORKDIR /home/py/app

COPY . .

RUN pip3 install virtualenv

RUN make setup

ENTRYPOINT ["python"]

EXPOSE 8083

CMD [ "app.py" ]
