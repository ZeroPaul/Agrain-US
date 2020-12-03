#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import io
import cv2
import math
import imutils as im
import numpy as ny

from imutils import perspective
from imutils import contours
from scipy.spatial import distance as dist

from .viewImage import viewImage
from .viewImage import viewShow

def mid_point(pointX, pointY):
    return ((pointX[0] + pointY[0]) * 0.5, (pointX[1] + pointY[1]) * 0.5)


def split_sample(image_file):
    image_list = {}
    grains = {}
    base_media = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_file = base_media + image_file
    image_master = cv2.imread(image_file)
    
    image_gray = cv2.cvtColor(image_master.copy(), cv2.COLOR_BGR2GRAY)
    image_rgb = cv2.cvtColor(image_master.copy(), cv2.COLOR_BGR2RGB)
    image_copy = image_rgb.copy()
    image_outline = image_rgb.copy()
    image_blur = cv2.GaussianBlur(image_gray, (3, 3), cv2.BORDER_DEFAULT)
    image_canny = cv2.Canny(image_blur, 50, 150)
    outlines, hierarchies = cv2.findContours(
        image_canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    grain_counter = 0
    pixels_milimeter = 24.257

    for outline in outlines:
        image_list_detail = []
        measures_grain = {}
        area = cv2.contourArea(outline)
        if area > 24.0:
            grain_counter += 1
            x, y, w, h = cv2.boundingRect(outline)
            crop_image = image_copy[y:y+h, x:x+w]

            cv2.drawContours(image_outline, [outline], 0, (0, 255, 0), 1, cv2.LINE_AA)
            
            box = cv2.minAreaRect(outline)
            box = cv2.boxPoints(box) if im.is_cv2() else cv2.boxPoints(box)
            box = ny.array(box, dtype="int")
            box = perspective.order_points(box)

            (tl, tr, br, bl) = box
            (tltrX, tltrY) =  mid_point(tl, tr)
            (blbrX, blbrY) = mid_point(bl, br)
            (tlblX, tlblY) = mid_point(tl, bl)
            (trbrX, trbrY) = mid_point(tr, br)

            dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
            dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

            dim_width = dA / pixels_milimeter
            dim_height = dB / pixels_milimeter

            measures_grain['area'] = area
            measures_grain['width'] = dim_width
            measures_grain['height'] = dim_height
            measures_grain['image'] = crop_image
            g_c = str(grain_counter)
            grains[grain_counter] = measures_grain

    # is_success, buffer = cv2.imencode(".jpg", image_outline)
    # io_buf = io.BytesIO(buffer)
    # image_list['image_border'] = io_buf
    image_list['total_grains'] = grain_counter
    image_list['grains_result'] = grains
    
    return image_list

# file_name = 'Tester4.jpg'
# print(split_sample(file_name))
