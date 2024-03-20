FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
#COPY docker/entrypoint.sh /docker/entrypoint.sh
RUN apt-get update && \
    apt-get install -y gcc libavdevice-dev libavfilter-dev libopus-dev libvpx-dev pkg-config netcat-traditional && \
    apt-get install -y binutils libproj-dev gdal-bin
COPY requirements.txt /app/requirements.txt


RUN pip install -r requirements.txt && pip install --upgrade pip setuptools
COPY . /app

EXPOSE 8000