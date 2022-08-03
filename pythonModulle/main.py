import warnings
warnings.filterwarnings('ignore')
import os
import sys
import json
import datetime
import numpy as np
import skimage.draw

import random
import math
import re
import time
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg

from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
from mrcnn.visualize import display_instances
import mrcnn.model as modellib
from mrcnn.model import log
from mrcnn.config import Config
from mrcnn import model as modellib, utils



# Root directory of the project
ROOT_DIR = "C:\\DetectionCancer"

DEFAULT_LOGS_DIR = os.path.join(ROOT_DIR, "logs")

MODEL_DIR = os.path.join(ROOT_DIR, "logs")


WEIGHTS_PATH = "C:\\DetectionCancer\\logs\\tumor_detector20211224T1310"   #path of trained module

class CustomConfig(Config):
    """ Configuration for training on the custom  dataset.
   
    """
    # name of config
    NAME = 'tumor_detector'
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 1 + 1  # background + tumor
    DETECTION_MIN_CONFIDENCE = 0.9    
    STEPS_PER_EPOCH = 10
    LEARNING_RATE = 0.001
    
      
#### Our Custom Dataset Classe **************************** ****************** * **********
class CustomDataset(utils.Dataset):

    def load_custom(self, dataset_dir, subset):
        """Load a subset 
        DATASET_DIR: Root directory of the dataset.
        subset: Subset to load: train or val folder
        """
        # Add classes. We have only one class to add.
        self.add_class("tumor", 1, "tumor")

        # Our Subset
        assert subset in ["train", "val"]
        dataset_dir = os.path.join(dataset_dir, subset)

        annotations1 = json.load(open('C:\\DetectionCancer\\brain-tumor\\data_cleaned\\train\\annotations_train.json'))
        annotations = list(annotations1.values()) 

        # annotation Image
        annotations = [a for a in annotations if a['regions']]

        # Add images
        for a in annotations:
            # Get the x, y coordinaets (BOUNDING BOX) of points of the polygons 
            # the outline of each object instance. These are stores in the
            # IF FOR solve problem of migration in the tensorflow version
            if type(a['regions']) is dict:
                polygons = [r['shape_attributes'] for r in a['regions'].values()]
            else:
                polygons = [r['shape_attributes'] for r in a['regions']]

            
            # the image. This is only managable since the dataset is tiny.
            image_path = os.path.join(dataset_dir, a['filename'])
            image = skimage.io.imread(image_path)
            height, width = image.shape[:2]

            self.add_image(
                "tumor",
                image_id=a['filename'],  
                path=image_path,
                width=width, 
                height=height,
                polygons=polygons
            )

    def load_mask(self, image_id):
        """Generate instance masks for an image.
       Returns:
        class_ids: a 1D array of class IDs of the instance masks.
        """
        # If not a farm_cow dataset image, delegate to parent class.
        image_info = self.image_info[image_id]
        if image_info["source"] != "tumor":
            return super(self.__class__, self).load_mask(image_id)

        # Convert polygons to a bitmap mask of shape
        # [height, width, instance_count]
        info = self.image_info[image_id]
        mask = np.zeros([info["height"], info["width"], len(info["polygons"])],
                        dtype=np.uint8)
        for i, p in enumerate(info["polygons"]):
            # Get indexes of pixels inside the polygon and set them to 1
            rr, cc = skimage.draw.polygon(p['all_points_y'], p['all_points_x'])
            mask[rr, cc, i] = 1

        # Return mask, and array of class IDs of each instance. Since we have
        # one class ID only, we return an array of 1s
        return mask.astype(np.bool), np.ones([mask.shape[-1]], dtype=np.int32)

    def image_reference(self, image_id):
        """Return the path of the image """
        info = self.image_info[image_id]
        if info["source"] == "tumor":
            return info["path"]
        else:
            super(self.__class__, self).image_reference(image_id)

# Inspect the model in training or inference modes values: 'inference' or 'training'
TEST_MODE = "inference"
ROOT_DIR = "C:\\DetectionCancer\\brain-tumor\\data_cleaned"

 #Resize image input to 16*16 pixel
def get_ax(rows=1, cols=1, size=16):
  
  _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
  return ax
#  
#  Main programme **************** 

# Load validation dataset
CUSTOM_DIR = "C:\\DetectionCancer\\brain-tumor\\data_cleaned"
dataset = CustomDataset()
dataset.load_custom(CUSTOM_DIR, "train")
dataset.prepare()

config = CustomConfig()
#LOAD MODEL. Create model in inference mode #  MODEL_DIR
model = modellib.MaskRCNN(mode="inference", model_dir= DEFAULT_LOGS_DIR  , config=config)
# Load COCO weights Or, load the last model you trained
weights_path =model.find_last()     # WEIGHTS_PATH
# Load weights
print("Loading weights ", weights_path)
model.load_weights(weights_path, by_name=True)

# choose Image to predect the Tumomr of it
path_to_new_image = 'C:\\DetectionCancer\\brain-tumor\\data_cleaned\\train\\7.jpg'
image1 = mpimg.imread(path_to_new_image)

# Run object detection
results1 = model.detect([image1], verbose=0)
r1 = results1[0]

# ********************* Display Result ********************* 
visualize.display_instances(
    image1, 
    r1['rois'], 
    r1['masks'], 
    r1['class_ids'],
    dataset.class_names, 
    r1['scores'], 
    # ax=get_ax(), 
    title="Image Detected",
    colors=visualize.random_colors(len(['#c51d1d', '#d42b2b', '#ec0c0c', '#f32d2d', '#e91111'])),
    show_mask=True,
    show_bbox=True
)