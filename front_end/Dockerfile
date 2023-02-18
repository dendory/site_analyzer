FROM python:3.9
WORKDIR /front_end
COPY . /front_end
RUN pip install --no-cache-dir -r ./front_end/requirements.txt
EXPOSE 5000
CMD ["python", "front_end.py"]
