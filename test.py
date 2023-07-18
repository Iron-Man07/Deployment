import sys
import io
from PIL import Image
import cv2
import torch
from flask import Flask, render_template, request, make_response
from werkzeug.exceptions import BadRequest
import os

app = Flask(__name__)

dictOfModels = {}
listOfKeys = []

def get_prediction(img_bytes,model):
    img = Image.open(io.BytesIO(img_bytes))
    results = model(img, size=640)  
    return results
    
@app.route('/', methods=['GET'])
def get():
  return render_template("index.html", len = len(listOfKeys), listOfKeys = listOfKeys)
  
@app.route('/', methods=['POST'])
def predict():
    file = extract_img(request)
    img_bytes = file.read()
    results = get_prediction(img_bytes,dictOfModels["best"])
   
    results.render()
    for img in results.ims:
        RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im_arr = cv2.imencode('.jpg', RGB_img)[1]
        response = make_response(im_arr.tobytes())
        response.headers['Content-Type'] = 'image/jpeg'
    return response

def extract_img(request):
    if 'file' not in request.files:
        raise BadRequest("Missing file parameter!")
    file = request.files['file']
    if file.filename == '':
        raise BadRequest("Given file is invalid")
    return file
    
    
    
if __name__ == '__main__':
    best_model_path ='best.pt'
    # models_directory = '/home/rnil/model/weights/'

  

    dictOfModels["best"] = torch.hub.load('ultralytics/yolov5', 'custom', path=best_model_path, force_reload=True)
    for key in dictOfModels :
        listOfKeys.append(key)
    
    app.run(host='0.0.0.0', port= 8080)
