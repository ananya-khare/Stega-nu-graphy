from flask import Flask,request,redirect,url_for,flash,render_template,send_from_directory
import os
import uuid
from werkzeug.utils import secure_filename
import subprocess
import glob

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
OUTPUT = os.path.join(os.getcwd(), "output")
IMAGES = os.path.join(UPLOAD_FOLDER,'img')
EXTRACT = os.path.join(UPLOAD_FOLDER,'temp')

TEXTS = os.path.join(UPLOAD_FOLDER,'txt')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = "asdasdiu3020"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No cover file"
        if 'to_hide' not in request.files:
            return "No embed file submitted"
        file = request.files['file']
        to_hide = request.files['to_hide']
        password = request.form['password']
        if file.filename == "" or to_hide.filename == "":
            return redirect(url_for('index'))
        if file and allowed_file(file.filename) and to_hide:
            ext = file.filename.split('.')[-1]
            id = str(uuid.uuid4())
            filename = id+"."+ext
            ###########################
            #Save temp files
            file.save(os.path.join(IMAGES,filename))
            to_hide.save(os.path.join(TEXTS,id+".txt"))
            ############################
            #Hide file
            os.chdir(os.path.join(os.getcwd()))
            subprocess.run(['steghide','embed','-ef',"../uploads/txt/"+id+".txt","-cf","../uploads/img/"+filename,"-sf",filename,"-p",password])
            return send_from_directory(OUTPUT,filename,as_attachment=True)
    return render_template('index.html')