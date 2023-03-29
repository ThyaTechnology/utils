# ThyaTech utils

## Create environment

```bash
conda create -y -n ThyaTech-utils python=3.9
conda activate ThyaTech-utils
pip install opencv-python
```

## crop images

```bash
python crop.py --image balloon.jpg --xyxy 600 350 750 500 --image_out crop.jpg
python crop.py --image balloon.jpg --xywh 600 350 150 150 --image_out crop.jpg
```
