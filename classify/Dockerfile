FROM python:3

COPY requirements.txt classify/requirements.txt
RUN pip install -r classify/requirements.txt

# RUN apt-get update
# RUN apt-get install tesseract-ocr poppler-utils -y

WORKDIR /classify

#ADD extract_contents.py /extract_data
RUN wget https://download.pytorch.org/models/alexnet-owt-4df8aa71.pth -P /root/.cache/torch/checkpoints/

COPY . /classify

ENTRYPOINT ["python", "./classify.py"]