# ThyaTech utils

This repository contains utility function to process images.

## Create environment

```bash
conda create -y -n ThyaTech-utils python=3.9
conda activate ThyaTech-utils
pip install opencv-python
pip install thya
```

## Crop images

### Description

```bash
usage: crop.py [-h] (--image IMAGE | --folder FOLDER) (--xyxy XYXY [XYXY ...] | --xywh XYWH [XYWH ...]) (--image_out IMAGE_OUT | --folder_out FOLDER_OUT) [--overwrite]

optional arguments:
  -h, --help            show this help message and exit
  --image IMAGE         Path of an image to crop. (default: None)
  --folder FOLDER       Path of a folder containing a list of images to crop. (default: None)
  --xyxy XYXY [XYXY ...]
                        Dimension of the rectangle to crop around, in the format X1Y1X2Y2. (default: None)
  --xywh XYWH [XYWH ...]
                        Dimension of the rectangle to crop around, in the format XYWH. (default: None)
  --image_out IMAGE_OUT
                        Path to save the cropped image. (default: None)
  --folder_out FOLDER_OUT
                        Path to of the folder to save the cropped images. (default: None)
  --overwrite           Force the write of the image(s) if already existing (default: False)
```

### Examples

```bash
python crop.py --image images/balloon1.jpg --xyxy 600 350 750 500 --image_out images_cropped/balloon1.jpg
python crop.py --image images/balloon1.jpg --xywh 600 350 150 150 --image_out images_cropped/balloon1.jpg
python crop.py --folder images --xyxy 600 350 750 500 --folder_out images_cropped
python crop.py --folder images --xywh 600 350 150 150 --folder_out images_cropped
```

### How to use

1. Clone this repository.

`git clone https://github.com/ThyaTechnology/utils.git`

2. Create a folder `path/to/images/to/crop` and place your images to crop in it.

3. Create a folder `path/to/images/once/cropped` where all your cropped images will be stored.

4. Create the python environement and install the libraries.

```bash
conda create -y -n ThyaTech-utils python=3.9
conda activate ThyaTech-utils
pip install opencv-python
```

5. Run the python code to crop your images.

`python crop.py --folder path/to/images/to/crop --xyxy 600 350 750 500 --folder_out path/to/images/once/cropped`


## Run remote inference


### Description

```bash
usage: infer.py [-h] (--image IMAGE | --folder FOLDER) [--project_id PROJECT_ID] [--api_key API_KEY]

optional arguments:
  -h, --help            show this help message and exit
  --image IMAGE         Path of an image to infer. (default: None)
  --folder FOLDER       Path of a folder containing a list of images to infer. (default: None)
  --project_id PROJECT_ID
                        ID of the project to infer from. (default: None)
  --api_key API_KEY     API key from www.thya-technology.com. (default: None)
```

### Examples

```bash
python infer.py --image images/balloon1.jpg --api_key <FROM_THYA> --project_id <FROM_THYA>
python infer.py --folder images --api_key <FROM_THYA> --project_id <FROM_THYA>
```

### How to use

1. Clone this repository.

`git clone https://github.com/ThyaTechnology/utils.git`

2. Create a folder `path/to/images/to/infer` and place your images to infer in it.

3. Create the python environement and install the libraries.

```bash
conda create -y -n ThyaTech-utils python=3.9
conda activate ThyaTech-utils
pip install opencv-python
pip install thya
```

4. Run the python code to crop your images.

`python infer.py --folder path/to/images/to/crop --api_key <FROM_THYA> --project_id <FROM_THYA>`
