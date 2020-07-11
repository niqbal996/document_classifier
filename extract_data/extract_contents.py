import pdf2image
import pytesseract
from os import path
from flask import Flask, render_template, request
app = Flask(__name__)

def get_image(pdf_file_path):
    return pdf2image.convert_from_path(pdf_file_path)

def extract_contents(pdf_path):
    image = get_image(pdf_path)
    # image_array = np.zeros((len(image), image[0].size[1], image[0].size[0], 3))
    # Extract contents and process page wise
    for n in range(len(image)): # number of pages in the pdf file
        # image_array[n, :, :, :] = np.array(image[0])
        contents = pytesseract.image_to_string(image[0])
        # print("hold")
    # contents = pytesseract.image_to_string(image_array[0])
    return contents

@app.route('/extract', methods=['GET'])
def display_extracted_data():
    if path.isfile(r'/extract_data/sample.pdf'):
        string_data = extract_contents(pdf_path=r'/extract_data/sample.pdf')
        return '[INFO] Following pdf data has been extract: <br/>' + string_data
    else:
        return '[INFO] No file found. '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
