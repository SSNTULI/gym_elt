FROM python:3.11-slim
WORKDIR /app
COPY "data_transform.py" .
RUN pip install pandas requests tqdm
ENTRYPOINT ["python", "data_transform.py"]