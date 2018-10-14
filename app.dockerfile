FROM python:3.7-alpine

RUN pip install pipenv

CMD pipenv install && pipenv run start_dev
