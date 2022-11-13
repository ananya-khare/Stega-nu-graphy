FROM python:3.8

WORKDIR /STEGA-NU-GRAPHY
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD [ "python", "./app.py"]