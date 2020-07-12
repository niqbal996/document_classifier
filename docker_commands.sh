#!/bin/bash
#sudo docker-compose down
sudo docker stop micro_file_input_1 micro_extract_data_1 micro_classify_1
sudo docker-compose build --no-cache
sudo docker-compose up