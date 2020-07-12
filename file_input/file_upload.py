from flask import Flask, render_template, request, redirect
from os.path import join
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      f.save(join("data", f.filename))#secure_filename
      return redirect('http://localhost:8000/extract')
         #'[INFO] File uploaded successfully.<br/> '+ join("data", f.filename)
		
if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')
