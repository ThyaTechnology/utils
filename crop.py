import cv2
import argparse
import os

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

action = parser.add_mutually_exclusive_group(required=True)
action.add_argument('--image', type=str,
                    help='Path of an image to crop.')
action.add_argument('--folder', type=str,
                    help='Path of a folder containing a list of images to crop.')

action = parser.add_mutually_exclusive_group(required=True)
action.add_argument('--xyxy', nargs='+', type=int,
                    help='Dimension of the rectangle to crop around, in the format X1Y1X2Y2.')
action.add_argument('--xywh', nargs='+', type=int,
                    help='Dimension of the rectangle to crop around, in the format XYWH.')

action = parser.add_mutually_exclusive_group(required=True)
action.add_argument('--image_out',
                    help='Path to save the cropped image.')
action.add_argument('--folder_out',
                    help='Path to of the folder to save the cropped images.')

parser.add_argument('--overwrite', action="store_true",
                    help='Force the write of the image(s) if already existing')
args = parser.parse_args()


IMG_EXT = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]

# If single image to process, add it to a list of 1 image
if args.image is not None:
    if not os.path.exists(args.image):
        raise Exception(f"The input image {args.image} does not exist.")
    path_images = [args.image]
    path_images_out = [args.image_out]


# If folder to process, add every image in the folder to the list of images top process
if args.folder is not None:
    if not os.path.exists(args.folder):
        raise Exception(f"The input folder {args.folder} does not exist.")
    path_images = [os.path.join(args.folder, f) for f in os.listdir(
        args.folder) if f.endswith(tuple(IMG_EXT))]
    path_images_out = [os.path.join(args.folder_out, f) for f in os.listdir(
        args.folder) if f.endswith(tuple(IMG_EXT))]


for path_image, path_image_out in zip(path_images, path_images_out):
    # Read an image
    img = cv2.imread(path_image)

    # get size rectangle
    if args.xyxy is not None and len(args.xyxy) == 4:
        x1, y1, x2, y2 = args.xyxy
        x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    elif args.xywh is not None and len(args.xywh) == 4:
        x, y, w, h = args.xywh
        x1, y1, x2, y2 = x, y, x+w, y+h
    elif args.xyxy is not None and len(args.xyxy) != 4:
        raise Exception(
            f"The argument `--xyxy` ({args.xyxy}) received {len(args.xyxy)} values but expect 4 values.")
    elif args.xywh is not None and len(args.xywh) != 4:
        raise Exception(
            f"The argument `--xywh` ({args.xywh}) received {len(args.xywh)} values but expect 4 values.")
    else:
        raise Exception(
            "Error in parsing the arguments of the retangle to crop.")
    # print(x1, y1, x2, y2)

    # perform cropping
    img_cropped = img[y1:y2, x1:x2]

    # check if output path already exists
    if os.path.exists(path_image_out) and not args.overwrite:
        raise Exception(
            f"The file {path_image_out} already exists. Use `--overwrite` to overwrite that file.")

    # create folder to store image if does not exist yet
    if os.path.dirname(path_image_out) != "":
        os.makedirs(os.path.dirname(path_image_out), exist_ok=True)

    # save cropped image
    cv2.imwrite(path_image_out, img_cropped)
