FROM python:3

COPY requirements.txt extract_data/requirements.txt
RUN pip install -r extract_data/requirements.txt

RUN apt-get update
RUN apt-get install tesseract-ocr poppler-utils -y

WORKDIR /extract_data

#ADD extract_contents.py /extract_data

COPY . /extract_data

ENTRYPOINT ["python", "./extract_contents.py"]
