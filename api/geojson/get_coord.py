import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lt_template.settings")

import django

django.setup()

from django.utils.html import strip_tags

from app.oilpipline.models import OilPipline

f = open('pipeline.json')

file_load = json.load(f)

for i in file_load['features']:
    print(i['properties']['clusterCaption'])
    if 'Нефтепровод' in i['properties']['clusterCaption']:
        print(i['properties']['clusterCaption'])
        oil = OilPipline.objects.create(
            name=i['properties']['clusterCaption'],
            description=strip_tags(i['properties']['balloonContentBody']).replace('&nbsp;', ' '),
            geo_type=i['type'],
            geometry=i['geometry'],
        )
