FROM public.ecr.aws/docker/library/python:3.9.19-alpine3.20

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./main.py /code/main.py

EXPOSE 80

CMD ["fastapi", "run", "main.py", "--port", "80"]

