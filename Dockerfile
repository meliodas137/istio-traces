FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN opentelemetry-bootstrap -a install
COPY . .
EXPOSE 5000
CMD ["/bin/sh", "-c", "opentelemetry-instrument --traces_exporter console --metrics_exporter console flask run --host=0.0.0.0"]
