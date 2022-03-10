FROM ubi8/python-39
COPY . /opt/app-root/src
RUN ls
RUN pip install -r /opt/app-root/src/requirements.txt
EXPOSE 5000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "5000"]

