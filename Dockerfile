FROM python: latest
COPY . ./
CMD ["python", "./testcicd.py"]