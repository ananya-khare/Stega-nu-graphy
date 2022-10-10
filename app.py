from flask import Flask,render_template,request,send_file
from PIL import Image
from steg import hide,unhide
from text import encode as encode_text
from text import decode as dcode
from io import BytesIO
app = Flask(__name__)

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG', quality=100)
    img_io.seek(0)
    return send_file(img_io,as_attachment=True,download_name='test', mimetype='image/png')