from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt

from sentinelhub import SHConfig

from sentinelhub import MimeType, CRS, BBox, SentinelHubRequest, SentinelHubDownloadClient, \
    DataCollection, bbox_to_dimensions, DownloadRequest
config = SHConfig()
config.sh_client_id = '31d94b8d-1a1f-45ce-aee3-e708d69cf0f5'
config.sh_client_secret = 'AnpU5L9fv{GL?fD4.tjiwBtpNV{jv_+@h4!Ih>b.'

if not config.sh_client_id or not config.sh_client_secret:
    print("Warning! To use Process API, please provide the credentials (OAuth client ID and client secret).")

import matplotlib.pyplot as plt
import numpy as np


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

betsiboka_coords_wgs84 = [74.44956331395248, 63.02904804600002, 74.46210459688555, 63.03484056516876]

resolution = 10
betsiboka_bbox = BBox(bbox=betsiboka_coords_wgs84, crs=CRS.WGS84)
betsiboka_size = bbox_to_dimensions(betsiboka_bbox, resolution=resolution)
print(f'Image shape at {resolution} m resolution: {betsiboka_size} pixels')

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

request_true_color = SentinelHubRequest(
    data_folder='img_dir',
    evalscript=evalscript_true_color,
    input_data=[
        SentinelHubRequest.input_data(
            data_collection=DataCollection.SENTINEL2_L2A,
            time_interval=('2020-06-12', '2020-06-13'),
        )
    ],
    responses=[
        SentinelHubRequest.output_response('default', MimeType.PNG)
    ],
    bbox=betsiboka_bbox,
    size=betsiboka_size,
    config=config
)
true_color_imgs = request_true_color.get_data(save_data=True)
plot_image(true_color_imgs[0][:, :, 2], factor=3.5/1e4, vmax=1)

