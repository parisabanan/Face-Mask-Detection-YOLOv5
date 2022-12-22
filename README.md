<h1 align="center">Face Mask Detection | YOLOv5</h1>

<p align="center">
    <img src="https://github.com/parisabanan/Face-Mask-Detection-YOLOv5/blob/main/images/result.jpg">
</p>  


### Overview : 
The purpose of this project is to create a Deep Learning model that identifies whether or not someone is wearing a mask. My model is based on YOLO's object detection algorithm, and I'm using the dataset from kaggle's website.


### Dataset : 
[Face Mask Detection Dataset](https://www.kaggle.com/datasets/parot99/face-mask-detection-yolo-darknet-format)

**The dataset consists of two classes :**

- with_mask
- without_mask

**The dataset is split into 3 sets :**

- Train : 5800 images
- Validation : 1000 images
- Test : 100 images
 

### How To Run : 
1. Clone the project.
2. Install "env.yml" using Conda. The first line of the yml file sets the new environment's name.

Run the following commands to install requirements and prepare your development environment.  

```
git clone https://github.com/parisabanan/Face-Mask-Detection-YOLOv5.git    # clone
cd Face-Mask-Detection-YOLOv5   
conda env create -f env.yml    # install requirements
```


### Inference : 
For inference, first run the following command in terminal, it runs the fastAPI app.

```
uvicorn app:app --reload    # run fastAPI app 
```
Then, to test model's result you can send a request to "http://localhost:8000/detect" using Postman and send an image file.


<p align="center">
    <img src="https://github.com/parisabanan/Face-Mask-Detection-YOLOv5/blob/main/images/postman.jpg">
</p>
