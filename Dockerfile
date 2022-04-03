FROM registry.twilio.com/library/base-python-36:3.6.8-2

WORKDIR /twilio-tv
COPY libs /twilio-tv/libs
COPY src /twilio-tv/src
COPY test /twilio-tv/test
COPY main /twilio-tv/main
COPY requirements.txt /twilio-tv/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000
ENV PYTHONPATH "${PYTHONPATH}:/twilio-tv/"
ENTRYPOINT ["python"]
CMD ["/twilio-tv/main/main.py"]