from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']

    if file.filename == '':
        return 'No file selected'

    img = Image.open(file)
    # Konversi gambar RGBA menjadi RGB
    img = img.convert("RGB")
    img.save('static/uploaded_image.jpg')  # Menyimpan gambar yang diunggah

    return render_template('crop.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/crop', methods=['POST'])
def crop():
    x = int(request.form['x'])
    y = int(request.form['y'])
    width = int(request.form['width'])
    height = int(request.form['height'])

    img = Image.open('static/uploaded_image.jpg')
    cropped_img = img.crop((x, y, x + width, y + height))
    cropped_img.save('static/cropped_image.jpg')  # Menyimpan gambar yang dipotong

    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
