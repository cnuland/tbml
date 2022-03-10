FROM ubi8/python-39
COPY . /opt/app-root/src
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "5000"]

