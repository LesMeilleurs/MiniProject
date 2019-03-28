FROM python:3.7-alpine
WORKDIR /myapp
ADD . /myapp
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "aqcurrent.py"]