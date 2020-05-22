FROM python:latest
WORKDIR /home/kumaraman/pipeline/
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
