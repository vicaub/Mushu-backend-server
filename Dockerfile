# Production Builder
FROM python:3.7 as builder
WORKDIR /build

RUN pip3 install pipenv
ADD Pipfile Pipfile.lock ./

ENV PYTHONUSERBASE /pyroot
ENV PIP_USER 1

RUN pipenv install --deploy --system


# Production
FROM python:3.7-slim as production
RUN apt-get update && apt install -y python3-certifi && rm -rf /var/lib/apt/lists/*
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PATH /usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin:/pyroot/bin

ENV PYTHONPATH /pyroot/lib/python3.7/site-packages:/usr/lib/python3/dist-packages

COPY --from=builder /pyroot/ /pyroot/

ADD server server

CMD gunicorn -b 0.0.0.0:5000 -w 4 server.server:app


# Test builder
FROM builder as test-builder
RUN pipenv install --deploy --system -d


# Test
FROM production as test
COPY --from=test-builder /pyroot/ /pyroot/
ENV PYTHONUNBUFFERED 1
ENV PATH /usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin:/pyroot/bin

ENV PYTHONPATH /pyroot/lib/python3.7/site-packages:/usr/lib/python3/dist-packages:/app
CMD sh -c "python3 -m unittest discover ./tests"

COPY tests tests
