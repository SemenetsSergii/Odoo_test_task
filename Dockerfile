FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "odoo/odoo-bin", "-c", "./addons/odoo.conf"]