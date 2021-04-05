FROM ubuntu:latest
MAINTAINER NAME projects@ashwin.lol

RUN sudo apt update

#! PostgresSQL Setup (https://docs.docker.com/engine/examples/postgresql_service/)
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3
USER postgres
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER admin WITH SUPERUSER PASSWORD 'Oniichan';" &&\
    createdb -O docker docker
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf
EXPOSE 5432
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]

#! Flask Setup (https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04)
FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine-2020-12-19
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
# Debug variable
ENV FLASK_DEBUG True
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
