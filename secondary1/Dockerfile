FROM python:3.7-alpine
WORKDIR /secondary1
ENV FLASK_APP=app1.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 6000
COPY . .
CMD ["python", "app1.py"]
