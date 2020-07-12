# document_classifier

This project runs a browser-based flask app which can take a pdf file from user and extract data from it and then classify it using DeepDocc classifier.

# Dependencies (tested on Linux)
* docker
* docker-compose
# Setup 

Before setting up the docker images, download the following models and move them into the **classify** folder
* [Pretrained AlexNet](https://drive.google.com/file/d/1pyOxvQQrHwknhpc6guWp73-5E3eel0sh/view?usp=sharing)
* [Trained network](https://drive.google.com/file/d/1KhC12anJXDE7CAcls7ytQbVaywRf48b5/view?usp=sharing) after only 2 epochs.

Run the **docker_commands.sh** script which will use docker-compose to build the python images.  
```
chmod +x docker_commands.sh
./docker_commands.sh
```
This script will build and launch your docker microservices containers. 


# Usage

To test the scripts, go to your browser and type the following URL:

```http://localhost:5000/upload```

It should look like below image:

<img src="/images/upload.png" alt="File upload"/>

Now you can upload your pdf file and it will display its contents extracted. 

<img src="/images/extract.png" alt="File extract"/>

To see, the result of the **classification microservice** go to the following URL:

```http://localhost:9000/classify```

You will see the result of classification page-wise on this page. A sample result for a 2-page pdf is shown below:

<img src="/images/classify.png" alt="File classify"/>
