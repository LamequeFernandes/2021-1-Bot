FROM python:3.8-slim

RUN python -m pip install rasa==2.8.3

ADD ./bot /app
ADD ./start_services.sh /app

WORKDIR /app

USER root

ENTRYPOINT [  ]

RUN chmod +x /app/start_services.sh

CMD /app/start_services.sh