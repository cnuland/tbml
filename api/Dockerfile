FROM ubi8/python-39
COPY api/. /opt/app-root/src
RUN ls
RUN pwd
RUN pip install -r api/requirements.txt
EXPOSE 5000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "5000"]

