FROM python:3.12

ENV DEBIAN_FRONTEND=noninteractive
ENV PROJECT_DIR=/app

WORKDIR ${PROJECT_DIR}

RUN apt-get update \
    && apt-get dist-upgrade -y \
    && rm -rf /var/lib/apt/lists/* \

RUN pip install --upgrade pip \
    && pip install pipenv

COPY Pipfile* ${PROJECT_DIR}/

RUN pipenv install --system --deploy

COPY src ${PROJECT_DIR}/

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["main.py"]
