FROM python:3-slim

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY fetch_file_path.py /fetch_file_path.py

CMD ["python", "/fetch_file_path.py"]