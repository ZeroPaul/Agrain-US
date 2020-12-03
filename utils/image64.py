#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from io import BytesIO
import base64


def encode_image(path_image):
    image_load = Image.open(path_image)
    buffered = BytesIO()
    image_load.save(buffered, format='PNG')
    image_encoded = base64.b64encode(buffered.getvalue()).decode("utf-8")
    image = 'data:image/jpg;base64,' + image_encoded
    return image

def decode_image(path_image):
    pass
