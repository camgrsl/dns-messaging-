FROM python:3.7-alpine

WORKDIR /server
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install -r requirements.txt
EXPOSE $DNS_SERVER_PORT

CMD [ "python", "-u", "./run_server.py" ]