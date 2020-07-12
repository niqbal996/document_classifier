import pdf2image
import pytesseract
from os import path
from flask import Flask, request, render_template
app = Flask(__name__)

def get_image(pdf_file_path):
    return pdf2image.convert_from_path(pdf_file_path)

def extract_contents(pdf_path):
    image = get_image(pdf_path)
    # Extract contents and process page wise
    contents = ''
    for n in range(len(image)): # number of pages in the pdf file
        contents += pytesseract.image_to_string(image[n])+'\n'

    return contents

@app.route('/extract', methods=['GET'])
def display_extracted_data():
    if path.isfile(r'data/sample.pdf'):
        print("Before writing the file")
        string_data = extract_contents(pdf_path=r'data/sample.pdf')
        print("After writing the file")
        return '[INFO] Following pdf data has been extracted: <br/>' + string_data
    else:
        return '[INFO] No file found. '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
