FROM python:alpine

ENV APP_HOME=/app NAME='Fernando'
WORKDIR ${APP_HOME}

COPY IC.py README.md Memory.py instructions.code Clock.py bios.yml ./

CMD [ "./IC.py" ]
ENTRYPOINT [ "python" ]