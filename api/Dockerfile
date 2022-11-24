FROM python:3.7-alpine
WORKDIR /api
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3000
CMD ["python", "./app.py"]