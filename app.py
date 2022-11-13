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

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == "POST":
        image = request.files['image']
        pil_image = Image.open(image)
        rgb_image = pil_image.convert('RGB')
        data = encode_text(request.form['hide'])
        img = hide(rgb_image,data)
        decoded = unhide(img)
        decoded = decoded[:decoded.index("0000000")]
        return serve_pil_image(img)
    return render_template('index.html')

@app.route('/decode',methods = ['POST','GET'])
def decode_image():
    if request.method == "POST":
        image = request.files['image']
        pil_image = Image.open(image)
        decoded = unhide(pil_image)
        decoded = decoded[:decoded.index("0000000")]
        return str(dcode(decoded))
    return render_template('decode.html')


if __name__ == "__main__":
    app.run(debug=True,port=8000,host="0.0.0.0")