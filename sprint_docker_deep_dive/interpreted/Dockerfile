FROM python:3.7.4

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY demo app

WORKDIR /app

ENV PATH /root/.local:$PATH

EXPOSE 8000

CMD ["python", "-m", "gunicorn", "--bind", ":8000", "--workers", "1", "demo.wsgi"]