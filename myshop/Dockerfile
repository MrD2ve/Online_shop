FROM python:3.12

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /shop_app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /shop_app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]