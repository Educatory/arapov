import gzip
import pickle
from decimal import Decimal, getcontext

from django.conf import settings

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lt_template.settings")

import django
django.setup()

import glob

datasets_dir = os.path.normpath('../datasets')


def get_bbox():
    bboxes = glob.glob(datasets_dir + '/*/*/*/*bbox.pkl.gz')
    coords = []
    for bbox_file in bboxes:
        bbox_gzip = gzip.GzipFile(bbox_file, "r")
        bbox = pickle.load(bbox_gzip)

        c_dict = {
            'max_x': bbox.max_x,
            'max_y': bbox.max_y,
            'min_x': bbox.min_x,
            'min_y': bbox.min_y
        }
        coords.append(c_dict)
    return coords


if __name__ == '__main__':
   get_bbox()