import config
import numpy as np
import flask
from flask import Flask, request, render_template
from src.preprocessor import process
from src.db import main
import keras
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload',methods=['POST'])
def create():
    if 'image' not in request.files:
        return 'no files part'
    
    image = request.files['image']
    bytes_data = image.read()
    with open("src\image.jpg", "wb") as binary_file:
        binary_file.write(bytes_data)
    
    flat_array = process()
    ann =keras.models.load_model("src\\artifacts\\nn.h5")
    prediction = ann.predict(flat_array)
    result = [np.argmax(i) for i in prediction]
    res = result[0]


    main(int(res))
    return render_template('result.html',result=res)


if __name__=='__main__':
    app.run(host="localhost", port=config.PORT, debug=config.DEBUG_MODE)