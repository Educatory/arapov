import tempfile
from io import BytesIO

from PIL import Image
from django.conf import settings
import os

from django.core.files import File

from api.parse_dataset import get_bbox

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lt_template.settings")
import django
django.setup()

import datetime
import numpy as np
import matplotlib.pyplot as plt
from sentinelhub import SHConfig
from app.sentinel.models import BBox as ArapovBBox, BBoxImage
from sentinelhub import MimeType, CRS, BBox, SentinelHubRequest, SentinelHubDownloadClient, \
    DataCollection, bbox_to_dimensions, DownloadRequest

import matplotlib.pyplot as plt
import numpy as np

# Конфигурация подключения Sentinel-hub
config = SHConfig()
config.sh_client_id = settings.SH_CLIENT_ID
config.sh_client_secret = 'AnpU5L9fv{GL?fD4.tjiwBtpNV{jv_+@h4!Ih>b.'
config.save()

coords = get_bbox()
def plot_image(image, factor=1.0, clip_range=None, **kwargs):
    """
    Utility function for plotting RGB images.
    """
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
    if clip_range is not None:
        ax.imshow(np.clip(image * factor, *clip_range), **kwargs)
    else:
        ax.imshow(image * factor, **kwargs)
    ax.set_xticks([])
    ax.set_yticks([])


evalscript_true_color = """
    //VERSION=3

    function setup() {
        return {
            input: [{
                bands: ["B02", "B03", "B04"]
            }],
            output: {
                bands: 3
            }
        };
    }

    function evaluatePixel(sample) {
        return [sample.B04, sample.B03, sample.B02];
    }

"""


for coord in coords:
    arapov_bbox, _ = ArapovBBox.objects.get_or_create(**coord)

    resolution = 10
    dirty_bbox = BBox(bbox=coord, crs=CRS.WGS84)
    dirty_bbox_size = bbox_to_dimensions(dirty_bbox, resolution=resolution)

    start_date = datetime.datetime.strptime('2021-05-01', '%Y-%m-%d').date()
    for dt in range(20):
        if dt == 0:
            first_date = start_date
        else:
            first_date = second_date
        second_date = first_date + datetime.timedelta(days=10)

        request_true_color = SentinelHubRequest(
            evalscript=evalscript_true_color,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL2_L2A,
                    time_interval=(first_date, second_date),
                )
            ],
            responses=[
                SentinelHubRequest.output_response('default', MimeType.PNG)
            ],
            bbox=dirty_bbox,
            size=dirty_bbox_size,
            config=config
        )

        array_img = request_true_color.get_data()
        img = Image.fromarray(array_img[0])

        tf = tempfile.NamedTemporaryFile()
        file_name = '{}.png'.format(os.path.basename(tf.name))
        blob_file = BytesIO()
        img.save(blob_file, 'PNG')

        bbox_img = BBoxImage.objects.create(bbox=arapov_bbox, date_start=first_date, date_end=second_date)

        bbox_img.image.save(file_name, File(blob_file), save=False)
        bbox_img.save()

