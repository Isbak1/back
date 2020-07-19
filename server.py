from flask import Flask
from flask_cors import CORS , cross_origin
from flask import request, render_template, send_from_directory
from flask import send_file
import os
from werkzeug.utils import secure_filename
import image

app = Flask(__name__)
#CORS(app)


@app.route('/upload', methods=['GET', 'POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        print(request.files)
        f = request.files['file']
        print(request.data)
        print(request.json)
        print(request.form)
        degre = int(request.form['degre'])
        contrast = int(request.form['contrast'])
        f.save(secure_filename(f.filename))
        filename = image.importation(f.filename, degre, contrast)
        #os.remove(filename)
        return send_file(filename, mimetype=f.content_type)
    else:
        return "<form method='Post' enctype='multipart/form-data'> degré:<input type='range' name='degre' /> contrast:<input type='number' name='contrast' />&nbsp<input type='file' name='file'>&nbsp <button type='submit'>valider</button></form>"

