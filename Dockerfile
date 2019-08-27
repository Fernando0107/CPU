FROM python:alpine

ENV APP_HOME=/app
WORKDIR ${APP_HOME}

COPY IC.py README.md Memory.py instructions.code Clock.py bios.yml ins2.code ins3.code ins4.code ins5.code ./

CMD [ "./IC.py" ]
ENTRYPOINT [ "python" ]