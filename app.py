from fastapi import FastAPI, File, UploadFile
from PIL import Image
import torch


def model_loader():
    model_weighs_path = "./yolov5/runs/train/exp/weights/best.pt"
    mask_detector = torch.hub.load('./yolov5', 'custom', path=model_weighs_path, source='local')
    return mask_detector


model = model_loader()
app = FastAPI()


@app.post('/detect')
def detect(file: UploadFile = File(...)):
    image = Image.open(file.file)
    result = model(image)
    result.show()
    pandas_res = result.pandas().xyxy[0]
    return pandas_res.to_dict()
