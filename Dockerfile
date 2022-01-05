FROM python:3.5.4
RUN pip install -r requirements.txt
CMD ["pytest -m smoke"]