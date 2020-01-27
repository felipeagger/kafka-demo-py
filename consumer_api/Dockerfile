FROM python:3.7

RUN mkdir -p /home/py/app

WORKDIR /home/py/app

COPY . .

RUN pip3 install -r requirements.txt --upgrade

ENTRYPOINT ["python"]

EXPOSE 8084

CMD [ "app.py" ]
