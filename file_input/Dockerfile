FROM python:3

ADD file_upload.py /

COPY requirements.txt file_input:/requirements.txt

RUN pip install -r file_input:/requirements.txt

WORKDIR /file_input

COPY . /file_input

ENTRYPOINT ["python", "./file_upload.py"]