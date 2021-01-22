FROM python:3.7-alpine3.9

RUN pip install pymongo
COPY fetchData.py /fetchData.py
RUN echo "*/10 * * * * python /fetchData.py" | crontab -

CMD ["crond","-f"]
