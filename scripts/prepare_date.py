import os
import shutil
import zipfile
from random import random, seed
from keras_preprocessing import image
from kaggle.api.kaggle_api_extended import KaggleApi

DATA_DIR = os.path.join(os.getcwd(), "data")
ZIPFILE = os.path.join(DATA_DIR, "train.zip")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
TRAIN_DATA_DIR = os.path.join(DATA_DIR, "train")
TEST_DATA_DIR = os.path.join(DATA_DIR, "test")

shutil.rmtree(DATA_DIR, ignore_errors=True)

api = KaggleApi()
api.authenticate()

api.competition_download_file("dogs-vs-cats", "train.zip", path=DATA_DIR)

with zipfile.ZipFile(ZIPFILE, "r") as zipref:
    zipref.extractall(RAW_DATA_DIR)

os.remove(ZIPFILE)

for subdir in [TRAIN_DATA_DIR, TEST_DATA_DIR]:
    for label in ["dogs", "cats"]:
        os.makedirs(os.path.join(subdir, label))

seed(1)
split_ratio = 0.25

for file in os.listdir(os.path.join(RAW_DATA_DIR, "train")):
    src = os.path.join(RAW_DATA_DIR, "train", file)

    if random() < split_ratio:
        dst_dir = TEST_DATA_DIR
    else:
        dst_dir = TRAIN_DATA_DIR

    if file.startswith("cat"):
        dst = os.path.join(dst_dir, "cats", file)
    elif file.startswith("dog"):
        dst = os.path.join(dst_dir, "dogs", file)
    else:
        continue

    img = image.load_img(src, target_size=(150, 150))
    x = image.img_to_array(img)
    image.save_img(dst, x, data_format="channels_last", file_format="jpeg", scale=False)

shutil.rmtree(RAW_DATA_DIR, ignore_errors=True)