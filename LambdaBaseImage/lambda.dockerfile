FROM python:3
# docker build -t python-app .
# docker run -it --rm --name my-running-app python-app

WORKDIR /lambda

COPY controller.py .
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# VOLUME ./:./

CMD [ "python", "controller.py" ]
