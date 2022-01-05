FROM python:3.5.4
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /workdir
WORKDIR /workdir
CMD ["pytest", "-m", "smoke", ""]