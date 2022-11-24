FROM python:3.7-alpine
WORKDIR /client
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["tail", "-f", "/dev/null"]