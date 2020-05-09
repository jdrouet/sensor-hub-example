FROM python:alpine

WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code

ENTRYPOINT [ "python", "-u", "main.py" ]
CMD [ "--help" ]
