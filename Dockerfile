FROM python:latest

COPY search-algo/binarysearch.py /

CMD [ "python", "./binarysearch.py" ]
