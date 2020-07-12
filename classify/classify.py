from numpy import array, stack, asarray
from PIL import Image
from collections import OrderedDict
from pdf2image import convert_from_path
from torch.nn import Linear,DataParallel
from os import listdir
import torch
from glob import glob
# import torch.backends.cudnn as cudnn
import torchvision.transforms as transforms
import torchvision.models as models
from flask import Flask, render_template, request
app = Flask(__name__)

def get_image(pdf_file_path):
    '''Get image from pdf'''
    return convert_from_path(pdf_file_path)

def to3channels(image):
    '''Convert single channel image to 3 channel image'''
    imarray = array(image)
    # stacked_img = stack((imarray,) * 3, axis=-1)
    three_channel_image = Image.fromarray(imarray, 'RGB')
    return three_channel_image

def classify(image):
    '''Classify the image among 10 categories'''
    model = models.alexnet(pretrained=True)
    # model = Model()
    class_vector = ['Advertisement','Email','Form','Letter','Memo','News','Note','Report','Resume','Scientific']
    num_input_features = model.classifier[6].in_features
    model.classifier[6] = Linear(num_input_features, 10)

    # model.cuda()
    # model = DataParallel(model, device_ids=range(torch.cuda.device_count()))
    state_dict = torch.load('checkpoint.pth', map_location=torch.device('cpu'))

    new_state_dict = OrderedDict()

    # Convert the model keys from gpu trained to cpu type so that we can load the dictionary into AlexNet
    for k, v in state_dict.items():
        if 'module' not in k:
            k = 'module.' + k
        else:
            k = k.replace('module.', '')
        new_state_dict[k] = v

    # load the modified dictionary
    model.load_state_dict(new_state_dict)
    model.eval()

    loader = transforms.Compose([transforms.Scale(277), transforms.ToTensor()])
    x = loader(image)  # Preprocess image
    x = x.unsqueeze(0)  # Add batch dimension

    output = model(x)  # Forward pass
    pred = torch.argmax(output, 1)  #
    return class_vector[pred]

@app.route('/classify', methods=['GET'])
def display_extracted_data():
    pdf_file = glob("data/*.pdf")
    image = get_image(pdf_file[0])
    result = ""
    for x in range(len(image)):
        image3channels = to3channels(image[x])
        class_result = classify(image3channels)
        result += '[INFO] Page {} classified as {} <br/>'.format(x, class_result)

    print("Inside Try block")
    return '{}'.format(result)
    # except Exception as e:
    #     print("Inside Exception block")
    #     return e

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='9000')
