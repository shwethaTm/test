FROM python:latest
COPY testcicd.py ./
CMD ["python", "./testcicd.py"]
