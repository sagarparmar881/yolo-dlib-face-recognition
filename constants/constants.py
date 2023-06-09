from collections import OrderedDict
import pickle
from helpers.person_tracker import PersonTracker
from helpers.centroid_tracker import CentroidTracker

BASEURL = 'https://localhost:5001/api'
CLASSESFILE = './files/class.names'
MODELCONFIG = './files/yolo.cfg'
MODELWEIGHTS = './files/yolov4-obj_final.weights'
ENCODINGS_PATH = './files/encodings.pickle'
FACE_DATASET_PATH = './files/face_dataset'
DETECTION_METHOD = 'hog'
TARGET_WH = 320
THRESHOLD = 0.85
NMS_THRESHOLD = 0.3


with open(ENCODINGS_PATH , 'rb') as f:
    DATA = pickle.load(f)

with open(CLASSESFILE , 'rt') as f:
    CLASSNAMES = f.read().rstrip('\n').split('\n')

cams_in_use = []

yolo_points = OrderedDict()
recognizer_points = OrderedDict()
person_ids = OrderedDict()
missing_staffs = OrderedDict()
pt = OrderedDict()
ct = CentroidTracker()
dicts = {"yolo_points": yolo_points,
         "recognizer_points": recognizer_points,
         "person_ids": person_ids}


def initialize():
    for i in cams_in_use:
        yolo_points[i] = []
        recognizer_points[i] = []
        missing_staffs[i] = OrderedDict()
        person_ids[i] = []
        pt[i] = PersonTracker()


# generalized function to add to dicts
def append(dict_name, to_add, cam_idx):
    dicts[dict_name][cam_idx].append(to_add)
    #print(dicts)


def clear_ordered_dicts():
    for i in cams_in_use:
        yolo_points[i].clear()
        recognizer_points[i].clear()
        person_ids[i].clear()
