FROM python:3.9.1
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc
RUN curl https://packages.microsoft.com/config/debian/10/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
RUN apt update
RUN ACCEPT_EULA=Y apt install -y msodbcsql17

WORKDIR /app
COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]
