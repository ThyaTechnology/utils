import cv2
import argparse
import os 

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# subparsers = parser.add_subparsers(
#     help='help for subcommand', dest="subcommand")

# # create the parser for the "command_1" command
# parser_a = subparsers.add_parser('command_1', help='command_1 help')
# parser_a.add_argument('--image', type=str, help='help for bar, positional')
# parser_a.add_argument('--image_out', type=str, help='help for bar, positional')

# # create the parser for the "command_2" command
# parser_b = subparsers.add_parser('command_2', help='help for command_2')
# parser_b.add_argument('--folder', type=str, help='help for b')
# parser_b.add_argument('--folder_out', type=str, action='store', default='', help='test')


action = parser.add_mutually_exclusive_group(required=True)
action.add_argument('--image', type=str,
                    help='image to crop')
action.add_argument('--folder', type=str,
                    help='image to crop')

action = parser.add_mutually_exclusive_group(required=True)
action.add_argument('--xyxy', nargs='+', type=int,
                    help='rectangle to crop')
action.add_argument('--xywh', nargs='+', type=int,
                    help='rectangle to crop')

action = parser.add_mutually_exclusive_group(required=True)
action.add_argument('--image_out',
                    help='output filename')
action.add_argument('--folder_out',
                    help='output folder')
args = parser.parse_args()


IMG_EXT = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]

if args.image is not None:
    if not os.path.exists(args.image):
        raise Exception(f"The image {args.image} does not exist")
    path_images = [args.image]
    path_images_out = [args.image_out]


if args.folder is not None:
    if not os.path.exists(args.folder):
        raise Exception(f"The folder {args.folder} does not exist")
    
    # path_images = []
    # path_images_out = []
    # for f in os.listdir(args.folder):
    #     if f.endswith(tuple(IMG_EXT)):
    #         filename, ext = os.path.splitext(f)
    #         path_images.append(f)
    #         path_images_out.append(f.remplace)
    # list_image = 
    path_images = [os.path.join(args.folder, f) for f in os.listdir(
        args.folder) if f.endswith(tuple(IMG_EXT))]
    path_images_out = [os.path.join(args.folder_out, f) for f in os.listdir(
        args.folder) if f.endswith(tuple(IMG_EXT))]
    
    # path_images = [args.image]
    # path_images_out = [args.image_out]


for path_image, path_image_out in zip(path_images, path_images_out):
    img = cv2.imread(path_image)

    if args.xyxy is not None:
        x1, y1, x2, y2 = args.xyxy
    elif args.xywh is not None:
        x, y, w, h = args.xywh
        x1, y1, x2, y2 = x, y, x+w, y+h
    print(x1, y1, x2, y2)
    img_cropped = img[y1:y2, x1:x2]
    os.makedirs(os.path.dirname(path_image_out), exist_ok=True)
    cv2.imwrite(path_image_out, img_cropped)
