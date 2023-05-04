from thya.apis import init_model, inference_model
import argparse
import json
import os

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

action = parser.add_mutually_exclusive_group(required=True)
action.add_argument('--image', type=str,
                    help='Path of an image to infer.')
action.add_argument('--folder', type=str,
                    help='Path of a folder containing a list of images to infer.')

parser.add_argument('--project_id', type=str, default=None,
                    help='ID of the project to infer from.')

parser.add_argument('--api_key', type=str, default="None",
                    help='API key from www.thya-technology.com.')

args = parser.parse_args()


IMG_EXT = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]


# If single image to process, add it to a list of 1 image
if args.image is not None:
    if not os.path.exists(args.image):
        raise Exception(f"The input image {args.image} does not exist.")
    path_images = [args.image]


# If folder to process, add every image in the folder to the list of images top process
if args.folder is not None:
    if not os.path.exists(args.folder):
        raise Exception(f"The input folder {args.folder} does not exist.")
    path_images = [os.path.join(args.folder, f) for f in sorted(os.listdir(
        args.folder)) if f.endswith(tuple(IMG_EXT))]


model = init_model(project_id = args.project_id,
                     api_key = args.api_key)

for path_image in path_images:

    ret = inference_model(model = model,
                        image_path = path_image)

    print(json.dumps(ret, indent=4))

